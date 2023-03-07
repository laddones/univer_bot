from aiogram.dispatcher.filters.state import StatesGroup, State


class Add_information(StatesGroup):
    add_type = State()
    add_link = State()
    add_description = State()


class Start_blocking(StatesGroup):
    get_link = State()


class Contact_information(StatesGroup):
    contact_phone_number = State()
    contact_email = State()
    contact_chose = State()



