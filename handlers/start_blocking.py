from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from config.loader import dp, anti_flood, bot, api_storage_module
from modules.models.schema import LinkType, CreateLinkSchema, GetLinkSchema
from modules.text_manage_module import enums, text_manage_module


async def send_new_report_api(call, link: GetLinkSchema):
    if link.link.startswith('@'):
        link.link = 't.me/' + link.link.replace('@', '')
    try:
        inline_btn_go = InlineKeyboardButton('🔗Перейти за посиланням!', url=link.link)
        inline_btn_done = InlineKeyboardButton('✅Вже поскаржився', callback_data=f'btn_report_done/{link.id}')
        inline_btn_skip = InlineKeyboardButton('⏭Пропустити', callback_data=f'btn_report_skip/{link.id}')
        inline_btn_blocked = InlineKeyboardButton('🚫Вже заблокований?', callback_data=f'btn_report_blocked/{link.id}')
        inline_send_report = InlineKeyboardMarkup().add(inline_btn_go)
        inline_send_report.add(inline_btn_done)
        inline_send_report.add(inline_btn_skip)
        inline_send_report.add(inline_btn_blocked)

        await bot.send_message(
            call.from_user.id,
            text_manage_module.TextManageModule.get_task_text(
                link=link,
            ),
            reply_markup=inline_send_report, parse_mode=ParseMode.HTML, disable_web_page_preview=True
        )

    except:
        inline_btn_done = InlineKeyboardButton('✅Вже поскаржився', callback_data=f'btn_report_done/{link.id}')
        inline_btn_skip = InlineKeyboardButton('⏭Пропустити', callback_data=f'btn_report_skip/{link.id}')
        inline_btn_blocked = InlineKeyboardButton('🚫Вже заблокований?', callback_data=f'btn_report_blocked/{link.id}')
        inline_send_report = InlineKeyboardMarkup()
        inline_send_report.add(inline_btn_done)
        inline_send_report.add(inline_btn_skip)
        inline_send_report.add(inline_btn_blocked)

        await bot.send_message(
            call.from_user.id,
            text_manage_module.TextManageModule.get_task_text(
                link=link
            ),
            reply_markup=inline_send_report, parse_mode=ParseMode.HTML, disable_web_page_preview=True
        )