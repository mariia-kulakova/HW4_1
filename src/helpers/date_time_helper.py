from datetime import date, timedelta

def days_ago(days_count):
    return date.today() - timedelta(days=days_count)
