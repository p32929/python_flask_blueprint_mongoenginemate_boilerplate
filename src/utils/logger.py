from datetime import datetime
from constants import Constants


class Logger:
    @staticmethod
    def log_including_time(*args):
        now = datetime.utcnow()
        final_str = ""
        for s in args:
            final_str = final_str + " : " + str(s)

        if Constants.PROD is None:
            print(f"{str(now)} : {final_str}")

    @staticmethod
    def log_without_time(*args):
        final_str = ""
        for s in args:
            final_str = final_str + " : " + str(s)

        if Constants.PROD is None:
            print(f"{final_str}")
