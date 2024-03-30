from datetime import datetime, timedelta
from typing import Any

import requests
from utils.logger import logger


@logger
def fetch_data_from_url(currency_pairs: str) -> dict[str, Any]:
    current_date = datetime.now()

    url = f"https://iss.moex.com/iss/statistics/engines/futures/markets/indicativerates/securities/{currency_pairs}.json"
    params = {
        "from": (current_date - timedelta(days=30)).strftime("%Y-%m-%d"),
        "till": current_date.strftime("%Y-%m-%d"),
        "iss.json": "extended",
        "callback": "JSON_CALLBACK",
        "clearing": "vk",
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()
