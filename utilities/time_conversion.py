import datetime


class TimeConversion:
    def __init__(self):
        pass

    @staticmethod
    def convert_milliseconds_to_time(milliseconds=0.0):
        """
        Converts milliseconds to a 00:00 time
        :return:
        """
        seconds = float(milliseconds) / 1000
        return str(datetime.timedelta(seconds=seconds))
