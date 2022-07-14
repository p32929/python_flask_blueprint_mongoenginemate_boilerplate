import mongoengine as me
from mongoengine_mate import ExtendedDocument


class UserSchema(ExtendedDocument):
    email = me.StringField(required=True)
    name = me.StringField(required=True)

    meta = {
        "strict": False,
    }
