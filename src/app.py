# Imports
from src.schemas.blocked_token_schema import BlockedTokenSchema
from src.connector import jwt


@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload):
    jti = jwt_payload["jti"]
    token = BlockedTokenSchema.col().find_one({"jti": jti})
    return token is not None
