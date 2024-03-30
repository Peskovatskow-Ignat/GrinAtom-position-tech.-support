import pandas as pd
from utils.logger import logger


@logger
def read_and_check_numeric_format(path_file: str, currency_pairs_1: str, currency_pairs_2: str) -> pd.DataFrame:
    data_frame = pd.read_excel(path_file)
    try:
        data_frame[[f"{currency_pairs_1}_rate", f"{currency_pairs_2}_rate", f"{currency_pairs_1}  {currency_pairs_2}"]].sum()
    except:
        raise ValueError("Ошибка при обработке данных")
    return data_frame
