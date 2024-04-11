"Главный файл запуска бота"
import asyncio

from aiogram import Bot, Dispatcher
from config import TOKEN, db_url, modules

bot = Bot(token=TOKEN)
dp = Dispatcher()


async def lifespan():
    from database import init as init_database

    await init_database(db_url, modules)
    print("База данных инициализирована")


from commands import commands_router


async def main():
    await lifespan()
    dp.include_router(commands_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
