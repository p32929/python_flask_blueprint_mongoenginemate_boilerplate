from src.schemas.user_schema import UserSchema
from src.modules.user.user_dtos import LogineUserBody


class UserService:

    @staticmethod
    def login(body: LogineUserBody):
        return UserSchema.col().find_one_and_update(
            {"email": body.email},
            {
                "$set": body.dict()
            }, upsert=True, new=True
        )

    @staticmethod
    def get_all():
        return list(UserSchema.col().find({}))
