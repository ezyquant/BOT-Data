from datetime import date

import botdata as bd

# Get holidays in 2020
bd.get_holidays(2020)

# Check if date is holiday
bd.is_business_day(date(2020, 1, 1))

# Get next business day
bd.next_business_day(date(2020, 1, 1), 1)
