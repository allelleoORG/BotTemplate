"Главный файл запуска бота"
import asyncio

from aiogram import Bot, Dispatcher
from config import token

bot = Bot(token=token)
dp = Dispatcher()


from commands import commands_router


async def main():
    dp.include_router(commands_router)
    await dp.start_polling(bot)


def run_bot():
    asyncio.run(main())


if __name__ == "__main__":
    run_bot()
