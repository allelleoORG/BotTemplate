from database.models import User


class UserRepository(object):
    @staticmethod
    async def exists_by_id(user_id: int) -> bool:
        return await User.exists(id=user_id)

    @staticmethod
    async def exists_by_telegram_id(telegram_id: int) -> bool:
        return await User.exists(telegram_id=telegram_id)

    @staticmethod
    async def create_user(telegram_id: int) -> None:
        await User.create(telegram_id=telegram_id)

    @staticmethod
    async def user_count() -> int:
        return len(await User.all())

    @staticmethod
    async def get_all_users() -> list[User]:
        return await User.all()
