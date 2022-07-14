from datetime import timedelta
from flask import Flask
from flask_jwt_extended import JWTManager
#
app = Flask(__name__)
app.config["DEBUG"] = False
app.config["CACHE_TYPE"] = "null"
app.config["JWT_SECRET_KEY"] = "super-secret"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=7)
jwt = JWTManager(app)
# BP REG
from src.modules.root.root_controller import root_controller
app.register_blueprint(root_controller, url_prefix='/')
from src.modules.user.user_controller import user_controller
app.register_blueprint(user_controller, url_prefix='/users')