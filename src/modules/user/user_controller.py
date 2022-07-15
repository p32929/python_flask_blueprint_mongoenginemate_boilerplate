from datetime import timezone, datetime
from flask import Blueprint, request
from flask_pydantic import validate
from src.modules.user.user_dtos import LogineUserBody
from src.schemas.blocked_token_schema import BlockedTokenSchema
from src.modules.user.user_service import UserService
from src.utils.responder import Responder
from flask_pydantic import validate
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, get_jwt
from flask_pydantic_docs import openapi_docs

user_controller = Blueprint('users', __name__)


@user_controller.get('/')
@jwt_required()
@openapi_docs()
def get_users():
    users = UserService.get_all()
    return Responder.send(users, 200)


@user_controller.get('/auth_test')
@jwt_required()
@openapi_docs()
def auth_test():
    current_user = get_jwt_identity()
    return current_user


@user_controller.post('/login')
@openapi_docs()
@validate()
def login(body: LogineUserBody):
    logged_in_user = UserService.login(body)
    # 
    identity = str(logged_in_user.get('_id'))
    access_token = create_access_token(identity)
    # 
    to_be_returned = {
        "access_token": access_token,
    }
    return to_be_returned


@user_controller.delete('/logout')
@jwt_required()
@openapi_docs()
def logout():
    jti = get_jwt()["jti"]
    now = datetime.now(timezone.utc)

    BlockedTokenSchema.col().insert_one({
        "jti": jti,
        "created_at": now,
    })
    return Responder.ok({"success": True})
