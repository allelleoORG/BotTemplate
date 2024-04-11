from aiogram import types
from aiogram.filters.command import CommandStart
from commands import commands_router
from repository import UserRepository


@commands_router.message(CommandStart())
async def command_start_hendler(message: types.Message):
    if not await UserRepository.exists_by_telegram_id(message.from_user.id):
        await UserRepository.create_user(message.from_user.id)
    await message.reply("Привет!")
