from aiogram import Bot, types
from aiogram.filters.command import Command, CommandObject
from aiogram.fsm.context import FSMContext
from commands import commands_router
from config import ADMIN_IDS
from keyboards import send_spam_keyboard
from repository import UserRepository
from states import AdminSpamCommandState


@commands_router.message(Command("spam"))
async def command_spam_hendler(
    message: types.Message, command: CommandObject, state: FSMContext
):
    if not message.from_user.id in ADMIN_IDS:
        return

    users_count = await UserRepository.user_count()

    await state.set_state(AdminSpamCommandState.message)
    await state.update_data(message=command.args)

    await message.reply(
        f"Вы уверены что хотите отправить текст:\n\n{command.args}\n\nВсем пользователям({users_count})",
        reply_markup=send_spam_keyboard,
    )


@commands_router.callback_query(AdminSpamCommandState.message)
async def send_spam_query(call: types.CallbackQuery, state: FSMContext, bot: Bot):
    if call.data == "spam_yes":
        await call.message.answer("Запуск рассылки")
        data = await state.get_data()

        users = await UserRepository.get_all_users()

        for user in users:
            await bot.send_message(chat_id=user.telegram_id, text=data["message"])

        await state.clear()
    else:
        await call.message.edit_text("Рассылка отменена")
        await state.clear()
