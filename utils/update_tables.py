from typing import Any

import pandas as pd
from utils.logger import logger
from openpyxl.styles import NamedStyle


@logger
def cell_alignment(worksheet: dict[str, Any], df_cours: pd.DataFrame) -> None:
    for i, col in enumerate(df_cours.columns):
        column_len = max(df_cours[col].astype(str).map(len).max(), len(col)) + 1
        worksheet.column_dimensions[chr(65 + i)].width = column_len


@logger
def apply_style(worksheet: dict[str, Any], df_cours: pd.DataFrame) -> None:
    money_style = NamedStyle(name="money", number_format="##0.00 ₽ ")
    for col in ["C", "F", "G"]:
        for row in range(2, len(df_cours) + 2):
            worksheet[f"{col}{row}"].style = money_style