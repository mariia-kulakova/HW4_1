from datetime import datetime, timedelta

def days_ago_str(days_count):
    return datetime.today() - timedelta(days=days_count)
