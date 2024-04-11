from aiogram import types

keyboard = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [
            types.InlineKeyboardButton(text="✅Да", callback_data="spam_yes"),
            types.InlineKeyboardButton(text="❌ Нет", callback_data="span_no"),
        ]
    ]
)
