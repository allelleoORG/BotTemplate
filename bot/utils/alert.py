import datetime

import telebot
from config import alert_bot_token

bot = telebot.TeleBot(token)


def send_alert(alert: str) -> None:
    bot.send_message(-1002018247819, alert, message_thread_id=9)


def send_log(log: str) -> None:
    bot.send_message(-1002018247819, log, message_thread_id=28)


def send_file(file_path):
    # Открываем файл
    with open(file_path, "rb") as file:
        # Отправляем файл пользователю
        bot.send_document(-1002018247819, file, message_thread_id=28)


async def generate_alert(message: str, Bot="@template"):
    alert = f"⛔Alert⛔\n[ Bot ]: {Bot}\n[ Message ]: {message}\n[ Time ]: {datetime.datetime.now()}\n#alert #{Bot.replace('@', '')}"
    send_alert(alert=alert)
    return


async def generate_log(message: str, Bot="@template"):
    log = f"📡Log📡\n[ Bot ]: {Bot}\n[ Message ]: {message}\n[ Time ]: {datetime.datetime.now()}\n#log #{Bot.replace('@', '')}"
    send_log(log=log)
    return
