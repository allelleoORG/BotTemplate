from aiogram.fsm.state import State, StatesGroup


class AdminSpamCommandState(StatesGroup):
    message = State()
