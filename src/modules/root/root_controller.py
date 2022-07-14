from flask import Blueprint
from src.modules.root.root_service import RootService

root_controller = Blueprint('main', __name__)


@root_controller.route('/')
def hello():
    return RootService.hello()

# We recommend not doing anything in the root module