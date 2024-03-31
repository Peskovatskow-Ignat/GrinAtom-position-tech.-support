from typing import Any

import pandas as pd

from utils.logger import logger


@logger
def filter_clearing_data(data: dict[str, Any]) -> list:
    securities_data = data[1].get("securities")[1]
    filtered_data = [date for date in securities_data if date["clearing"] == "vk"]
    return filtered_data


@logger
def create_dataframe(
    currency_pairs_1: str,
    currency_pairs_2: str,
    data_curs_1: list[dict[str, Any]],
    data_curs_2: list[dict[str, Any]],
) -> pd.DataFrame:

    return pd.DataFrame(
        {
            f"{currency_pairs_1}_tradedate": [
                date["tradedate"] for date in data_curs_1
            ],
            f"{currency_pairs_1}_tradetime": [
                date["tradetime"] for date in data_curs_1
            ],
            f"{currency_pairs_1}_rate": [date["rate"] for date in data_curs_1],
            f"{currency_pairs_2}_tradedate": [
                date["tradedate"] for date in data_curs_2
            ],
            f"{currency_pairs_2}_tradetime": [
                date["tradetime"] for date in data_curs_2
            ],
            f"{currency_pairs_2}_rate": [date["rate"] for date in data_curs_2],
        }
    )
