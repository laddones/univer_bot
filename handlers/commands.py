from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ParseMode

from config.loader import dp, api_storage_module, anti_flood
from keyboard import keyboards
from modules.models.schema import CreateClientSchema, UpdateClientSchema
from modules.text_manage_module import enums


@dp.message_handler(state='*', commands=['start'])
@dp.throttled(anti_flood, rate=1)
async def command_start(message: types.Message, state: FSMContext):
    client = CreateClientSchema(
        user_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name
    )
    await api_storage_module.create_client(client)
    client = UpdateClientSchema(
        user_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name
    )
    await api_storage_module.create_client(client)
    await message.answer(enums.TextEnum.START.format(first_name=message.from_user.first_name), reply_markup=keyboards.Btn_main_menu.list_btn, parse_mode=ParseMode.HTML)
