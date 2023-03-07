from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from enum import Enum

from modules.models.schema import LinkType


class Btn_text_menu(str, Enum):
    START_BLOCKING = '🚫 Розпочати блокування'
    ADD_INF = '📨 Додати на блокування'
    CALLBACK = '🤙Зворотній зв\'язок📱'
    ABOUT = '📜Про бота'
    SEND_MESSAGE = '👋 Канал'
    HELP = '🆘 Допомога ЗСУ'
    MENU = '🌍 Меню'


class Btn_text_controller_inf(str, Enum):
    SKIP = '⏭️Пропустить'


class Btn_main_menu:
    btn_start_blocking = KeyboardButton(Btn_text_menu.START_BLOCKING)
    btn_add_inf = KeyboardButton(Btn_text_menu.ADD_INF)
    btn_callback = KeyboardButton(Btn_text_menu.CALLBACK)
    btn_about = KeyboardButton(Btn_text_menu.ABOUT)
    btn_send_message = KeyboardButton(Btn_text_menu.SEND_MESSAGE)
    btn_help = KeyboardButton(Btn_text_menu.HELP)
    btn_main_menu = KeyboardButton(Btn_text_menu.MENU)
    list_btn = ReplyKeyboardMarkup(resize_keyboard=True)\
        .row(btn_start_blocking)\
        .row(btn_add_inf, btn_callback)\
        .row(btn_about, btn_send_message)\
        .row(btn_help)


class Btn_controller:
    btn_skip = KeyboardButton(Btn_text_controller_inf.SKIP)

    list_btn_req = ReplyKeyboardMarkup(resize_keyboard=True).row(Btn_main_menu.btn_main_menu)
    list_btn = ReplyKeyboardMarkup(resize_keyboard=True).row(Btn_main_menu.btn_main_menu, btn_skip)


class Btn_type_of_link:
    btn_telegram = KeyboardButton(LinkType.TELEGRAM)
    btn_facebook = KeyboardButton(LinkType.FACEBOOK)
    btn_youtube = KeyboardButton(LinkType.YOUTUBE)
    btn_tiktok = KeyboardButton(LinkType.TIKTOK)
    btn_twitter = KeyboardButton(LinkType.TWITTER)
    btn_instagram = KeyboardButton(LinkType.INSTAGRAM)
    btn_another = KeyboardButton("Інше")

    list_btn = ReplyKeyboardMarkup(resize_keyboard=True)\
        .row(btn_telegram, btn_facebook)\
        .row(btn_youtube, btn_tiktok)\
        .row(btn_instagram, btn_twitter)\
        .row(btn_another)\
        .row(Btn_main_menu.btn_main_menu)


class Btn_share_contact:
    btn_share_contact = KeyboardButton('Поширити контакт', request_contact=True)
    btn_share_contact_chose_true = KeyboardButton('Так', resize_keyboard=True)
    btn_share_contact_chose_false = KeyboardButton('Ні', resize_keyboard=True)

    list_btn_req = ReplyKeyboardMarkup(resize_keyboard=True) \
        .row(btn_share_contact, Btn_main_menu.btn_main_menu)
    list_btn_chose = ReplyKeyboardMarkup(resize_keyboard=True) \
        .row(btn_share_contact_chose_true, btn_share_contact_chose_false)






