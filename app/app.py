"Файл для запуска нашего приложения"

from multiprocessing import Process

from bot.app import run_bot
from web.app import run_app

if __name__ == "__main__":
    bot = Process(target=run_bot)
    web = Process(target=run_app)

    bot.start()
    web.start()

    bot.join()
    web.join()
