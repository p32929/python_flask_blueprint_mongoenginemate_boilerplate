import mongoengine as me
from mongoengine_mate import ExtendedDocument
from src.schemas.user_schema import UserSchema


class BlockedTokenSchema(ExtendedDocument):
    jti = me.StringField()
    created_at = me.DateTimeField()
    user = me.ReferenceField(UserSchema)

    meta = {
        'strict': False,
    }
