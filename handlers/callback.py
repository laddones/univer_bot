import re

from aiogram import types
from aiogram.dispatcher import FSMContext

from MS import state_m
from config.loader import dp, api_storage_module
from keyboard import keyboards
from modules.models.schema import UpdateClientSchema


@dp.message_handler(content_types=types.ContentType.CONTACT, state=state_m.Contact_information.contact_phone_number)
async def bot_function_phone(message: types.Message, state: FSMContext):
    if message.text == keyboards.Btn_text_menu.MENU:
        await message.answer(keyboards.Btn_text_menu.MENU.value,
                             reply_markup=keyboards.Btn_main_menu.list_btn)
        await state.finish()
        return

    if message.contact.user_id != message.from_user.id:
        await message.answer("Неправильний номер. Натисніть на кнопку відправки номеру.")
        return
    await message.answer("Введите свой email", reply_markup=keyboards.Btn_controller.list_btn_req)
    async with state.proxy() as data:
        data['phone_number'] = message.contact.phone_number
    await state_m.Contact_information.contact_email.set()


@dp.message_handler(state=state_m.Contact_information.contact_email)
async def bot_function_contact_email(message: types.Message, state: FSMContext):
    if message.text == keyboards.Btn_text_menu.MENU:
        await message.answer(keyboards.Btn_text_menu.MENU.value,
                             reply_markup=keyboards.Btn_main_menu.list_btn)
        await state.finish()
        return
    result = None
    if len(re.findall(r'[A-Za-z\d._-]+@[A-Za-z]+\.[a-zA-Z]+', message.text)) > 0:
        email = re.findall(r'[A-Za-z\d._-]+@[A-Za-z]+\.[a-zA-Z]+', message.text)[0]
        async with state.proxy() as data:
            data['email'] = email
        await message.answer(text=f"Ви впевнені що хочете зв'язатися з модераторами ?",
                             reply_markup=keyboards.Btn_share_contact.list_btn_chose)
        await state_m.Contact_information.contact_chose.set()
        return
    if result is None:
        await message.answer(text=f"Неправильна пошта. Спробуйте ще раз.")


@dp.message_handler(state=state_m.Contact_information.contact_chose)
async def bot_function_contact(message: types.Message, state: FSMContext):
    if message.text == keyboards.Btn_text_menu.MENU:
        await message.answer(keyboards.Btn_text_menu.MENU.value,
                             reply_markup=keyboards.Btn_main_menu.list_btn)
        await state.finish()
        return

    if message.text == 'Так':

        async with state.proxy() as data:
            user = UpdateClientSchema(
                user_id=message.from_user.id,
                first_name=message.from_user.first_name,
                last_name=message.from_user.last_name,
                username=message.from_user.username,
                phone_number=data.get('phone_number'),
                email=data.get('email'),
                status=True
            )
        await api_storage_module.update_client(user_schema=user)
        await message.answer('Ваша заявка успішно прийнята. Очікуйте коли модератори з вами зв\'яжуться.',
                             reply_markup=keyboards.Btn_main_menu.list_btn)
        await state.finish()
        return
    if message.text == 'Ні':
        await message.answer(keyboards.Btn_text_menu.MENU.value,
                             reply_markup=keyboards.Btn_main_menu.list_btn)
        await state.finish()
        return