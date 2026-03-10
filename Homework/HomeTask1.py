from datetime import datetime, date

def get_days_from_today(string_date):
    return (datetime.strptime(string_date, "%Y-%m-%d").date() - date.today()).days

string_date = "2026-03-11"
print(get_days_from_today(string_date))
