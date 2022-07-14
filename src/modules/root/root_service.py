
from constants import Constants


class RootService:

    @staticmethod
    def hello():
        return f"Hello from {Constants.APP_NAME}"
