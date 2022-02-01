from aiogram.utils import executor

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware

from config import settings, logger
from handlers import dp_py

bot = Bot(token=settings.py_bot_token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
dp.middleware.setup(LoggingMiddleware(logger))


async def on_shutdown(dp_py):
    await dp_py.storage.close()
    await dp_py.storage.wait_closed()
    logger.info('Storage close')


if __name__ == '__main__':
    try:
        executor.start_polling(dp_py, skip_updates=True, on_shutdown=on_shutdown)
    except Exception as e:
        print(e, "CHECK BOT_TOKEN SETTINGS IN .env")
