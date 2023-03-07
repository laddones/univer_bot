from aiogram import Dispatcher, Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import config_dev
from modules.api.api_storage import ApiStorage

storage = MemoryStorage()

bot = Bot(token=config_dev.API_TOKEN)
dp = Dispatcher(bot, storage=storage)
api_storage_module = ApiStorage(api_host=config_dev.API_HOST)


async def anti_flood(*args, **kwargs):
    m = args[0]
    await m.answer("Багато повідомлень.")