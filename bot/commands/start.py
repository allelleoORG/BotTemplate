from aiogram import types
from aiogram.filters.command import CommandStart
from commands import commands_router


@commands_router.message(CommandStart())
async def command_start_hendler(message: types.Message):
    await message.reply("Привет!")
