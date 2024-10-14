from datetime import datetime

'''
Standard datetime ops, when needed.
'''

def get_today() -> datetime:
    return datetime.today()

def str_datetime(datetime_str: str) -> datetime:
    return datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")

def datetime_str(datetime_obj: datetime) -> str:
    return datetime.strftime(datetime_obj, "%Y-%m-%d %H:%M:%S")
