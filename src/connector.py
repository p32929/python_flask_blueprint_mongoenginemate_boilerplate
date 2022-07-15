from src.modules.user.user_controller import user_controller
from src.modules.root.root_controller import root_controller
from datetime import timedelta
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_pydantic_docs import OpenAPI
#
app = Flask(__name__)
app.config["DEBUG"] = False
app.config["CACHE_TYPE"] = "null"
app.config["JWT_SECRET_KEY"] = "super-secret"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=7)
jwt = JWTManager(app)
# openapi
swagger = OpenAPI(endpoint="/docs/swagger/", ui='swagger', name="swagger", extra_props={
    "components": {
        "securitySchemes": {
            "bearerAuth": {
                "type": "http",
                "scheme": "bearer",
                "bearerFormat": "JWT",
            }
        }
    },
    "security": [{"bearerAuth": []}]
})
swagger.register(app)
redoc = OpenAPI(endpoint="/docs/redoc/", ui='redoc', name="redoc")
redoc.register(app)
# BP REG
app.register_blueprint(root_controller, url_prefix='/')
app.register_blueprint(user_controller, url_prefix='/users')
