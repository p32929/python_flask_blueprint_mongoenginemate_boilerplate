from flask import Blueprint
from src.modules.root.root_service import RootService
from flask_pydantic_docs import openapi_docs

root_controller = Blueprint('main', __name__)


@root_controller.route('/')
@openapi_docs()
def root_hello():
    return RootService.hello()

# We recommend not doing anything in the root module
