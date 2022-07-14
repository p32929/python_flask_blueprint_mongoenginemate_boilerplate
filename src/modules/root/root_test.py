from constants import Constants
import root_controller


def test_abc():
    assert root_controller.hello() == f"Hello from {Constants.APP_NAME}"
