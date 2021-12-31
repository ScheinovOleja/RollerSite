import datetime


def date_by_adding_business_days(add_days):
    business_days_to_add = add_days
    current_date = datetime.date.today()
    while business_days_to_add > 0:
        current_date += datetime.timedelta(days=1)
        weekday = current_date.weekday()
        if weekday >= 5:  # sunday = 6
            continue
        business_days_to_add -= 1
    return current_date


print(date_by_adding_business_days(5).strftime("%d.%m.%Y"))