"Тут будет ORM для работы с базой данных"

from tortoise import Tortoise


async def init(db_url: str, modules: dict[str, list[str]]) -> None:
    await Tortoise.init(db_url=db_url, modules=modules)
    await Tortoise.generate_schemas()
