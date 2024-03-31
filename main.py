import pandas as pd

from conf.config import settings
from utils.chech_rows import read_and_check_numeric_format
from utils.data_processing import create_dataframe, filter_clearing_data
from utils.logger import logger
from utils.plural_utils import count_num_rows
from utils.request import fetch_data_from_url
from utils.send_mail import send_email
from utils.update_tables import apply_style, cell_alignment


def main() -> None:
    currency_pairs_1, currency_pairs_2 = (
        settings.CURRENCY_PAIR_1,
        settings.CURRENCY_PAIR_2,
    )

    currency_data_1, currency_data_2 = fetch_data_from_url(
        currency_pairs_1
    ), fetch_data_from_url(currency_pairs_2)

    currency_data_1, currency_data_2 = filter_clearing_data(
        currency_data_1
    ), filter_clearing_data(currency_data_2)

    df_cours = create_dataframe(
        currency_pairs_1, currency_pairs_2, currency_data_1, currency_data_2
    )

    df_cours[f"{currency_pairs_1}  {currency_pairs_2}"] = (
        df_cours[f"{currency_pairs_1}_rate"] / df_cours[f"{currency_pairs_2}_rate"]
    )

    file_path = f'tables/cours{currency_pairs_1.replace("/", "_")}__{currency_pairs_2.replace("/", "_")}.xlsx'

    writer = pd.ExcelWriter(file_path, engine="openpyxl")
    df_cours.to_excel(writer, index=False, sheet_name="Sheet")
    writer.book
    worksheet = writer.sheets["Sheet"]

    cell_alignment(worksheet, df_cours)

    apply_style(worksheet, df_cours)

    writer.close()

    num_rows = count_num_rows(
        read_and_check_numeric_format(file_path, currency_pairs_1, currency_pairs_2)
    )

    send_email(file_path, num_rows)


if __name__ == "__main__":
    main()
