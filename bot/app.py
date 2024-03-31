"Главный файл запуска бота"
import asyncio

from aiogram import Bot, Dispatcher
from config import token

bot = Bot(token=token)
dp = Dispatcher()


from commands import commands_router


async def lifespan(dp: Dispatcher):
    dp.include_router(commands_router)
    return dp


async def main():
    dp = await lifespan(dp)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
