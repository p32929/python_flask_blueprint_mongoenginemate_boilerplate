import werkzeug.serving
from flask_cors import CORS
from constants import Constants
from src.connector import app
from src.utils.database_utils import DatabaseUtils


def run_server():
    cors = CORS(app)
    DatabaseUtils.init_local_db("pyproject")
    werkzeug.run_simple('127.0.0.1', int(Constants.PORT),
                        app, use_debugger=True, use_reloader=True)


if __name__ == '__main__':
    run_server()
