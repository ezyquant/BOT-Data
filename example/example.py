from datetime import date

import botdata as bd

# Get holidays in 2020
bd.get_holidays(2022)

# Check if date is business day
bd.is_business_day(date.today())

# Get next business day
bd.next_business_day(date.today(), 1)
