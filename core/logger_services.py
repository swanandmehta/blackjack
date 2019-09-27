# This service will be used for logging information
from datetime import datetime


def log(meg):
    """  Logs the events in system """
    date_time = datetime.now()
    date_time.strftime("%m/%d/%y %H:%M:%S")
    print(date_time.strftime("%m/%d/%y %H:%M:%S:%f") + " : " + meg)

