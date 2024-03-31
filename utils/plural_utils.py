import pandas as pd

from utils.logger import logger


@logger
def plural_form(num: int) -> str:
    if num % 10 == 1 and num % 100 != 11:
        return f"{num} строка"
    elif 2 <= num % 10 <= 4 and (num % 100 < 10 or num % 100 >= 20):
        return f"{num} строки"
    else:
        return f"{num} строк"


@logger
def count_num_rows(data_frame: pd.DataFrame) -> int:

    return data_frame.shape[0]
