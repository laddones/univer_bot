from aiogram import types
from aiogram.types import ParseMode

from MS import state_m
from config.loader import anti_flood, dp, bot, api_storage_module
from handlers.start_blocking import send_new_report_api
from keyboard import keyboards
from keyboard.keyboards import Btn_text_menu
from modules.models.schema import LinkClientStatus, CreateLinkClientSchema
from modules.models.text_enum import Texts
from modules.text_manage_module import enums


@dp.message_handler(state=None)
@dp.throttled(anti_flood, rate=1)
async def main_menu(message: types.Message):
    if message.text == Btn_text_menu.START_BLOCKING:
        response = await api_storage_module.get_link(message.from_user.id)
        await send_new_report_api(message, response)
        await message.answer('Розпочати')

    if message.text == Btn_text_menu.ADD_INF:
        await message.answer('Оберіть тип посилання для блокуваня.', reply_markup=keyboards.Btn_type_of_link.list_btn)
        await state_m.Add_information.add_type.set()

    if message.text == Btn_text_menu.CALLBACK:
        await message.answer('Поширити ваш номер телефона', reply_markup=keyboards.Btn_share_contact.list_btn_req)
        await state_m.Contact_information.contact_phone_number.set()
        return

    if message.text == Btn_text_menu.ABOUT:
        await message.answer('О')

    if message.text == Btn_text_menu.SEND_MESSAGE:
        await message.answer('Канал')

    if message.text == Btn_text_menu.HELP:
        await message.answer('Допомога')


@dp.callback_query_handler(text_contains="btn_report")
@dp.throttled(anti_flood, rate=1)
async def report_sender(call: types.CallbackQuery):
    link_id = call.data.split('/')[-1]
    if call.data.split('/')[0] == 'btn_report_done':
        link_action = LinkClientStatus.REPORTED
    elif call.data.split('/')[0] == 'btn_report_skip':
        link_action = LinkClientStatus.SKIPPED
    elif call.data.split('/')[0] == 'btn_report_blocked':
        link_action = LinkClientStatus.DELETED
    else:
        return
    response = await api_storage_module.update_link(CreateLinkClientSchema(
            link=int(link_id),
            client=call.from_user.id,
            link_status=link_action
        )
    )
    print(response)
    await bot.delete_message(call.from_user.id, call.message.message_id)
    new_link = await api_storage_module.get_link(call.from_user.id)
    if new_link:
        await send_new_report_api(call, link=new_link)
    else:
        await bot.send_message(
            call.from_user.id,
            enums.TextEnum.MSG_LATER,
            parse_mode=ParseMode.HTML
        )




