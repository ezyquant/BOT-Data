from datetime import date
from typing import List

import pandas as pd


def get_holidays(year: int) -> List[date]:
    df = pd.read_html(
        f"https://www.bot.or.th/English/FinancialInstitutions/FIholiday/Pages/{year}.aspx"
    )[0]
    # df should contains the following columns: Index, Day of week, Day of month, Month, Description

    df = df.dropna(axis=1, how="any", subset=[2, 3])
    df = df[~df[4].str.contains("cancelled", case=False, na=False)]

    date_str_ser = df[2].astype(str) + " " + df[3] + " " + str(year)
    # Remove non-ascii characters
    date_str_ser = date_str_ser.str.encode("ascii", "ignore").str.decode("ascii")

    return pd.to_datetime(date_str_ser).map(lambda x: x.date()).tolist()  # type: ignore


def is_holiday(date_: date) -> bool:
    return date_ in get_holidays(date_.year)


def is_business_day(date_: date) -> bool:
    return date_.weekday() < 5 and not is_holiday(date_)


if __name__ == "__main__":
    print(get_holidays(2020))
