from aiogram import types
from aiogram.dispatcher import FSMContext

from MS import state_m
from config.loader import dp, anti_flood, bot, api_storage_module
from keyboard import keyboards
from modules.models.schema import LinkType, CreateLinkSchema
from modules.text_manage_module import enums


@dp.message_handler(state=state_m.Add_information.add_type)
@dp.throttled(anti_flood, rate=1)
async def add_type_link(message: types.Message, state: FSMContext):
    if message.text == LinkType.TELEGRAM:
        await bot.send_message(message.from_user.id, enums.TextEnum.LINK_TELEGRAM,
                               reply_markup=keyboards.Btn_controller.list_btn_req)
        async with state.proxy() as data:
            data['type'] = message.text
        await state_m.Add_information.add_link.set()

    if message.text == LinkType.FACEBOOK:
        await bot.send_message(message.from_user.id, enums.TextEnum.LINK_FACEBOOK,
                               reply_markup=keyboards.Btn_controller.list_btn_req)
        async with state.proxy() as data:
            data['type'] = message.text
        await state_m.Add_information.add_link.set()

    if message.text == LinkType.YOUTUBE:
        await bot.send_message(message.from_user.id, enums.TextEnum.LINK_YOUTUBE,
                               reply_markup=keyboards.Btn_controller.list_btn_req)
        async with state.proxy() as data:
            data['type'] = message.text
        await state_m.Add_information.add_link.set()

    if message.text == LinkType.TIKTOK:
        await bot.send_message(message.from_user.id, enums.TextEnum.LINK_TIKTOK,
                               reply_markup=keyboards.Btn_controller.list_btn_req)
        async with state.proxy() as data:
            data['type'] = message.text
        await state_m.Add_information.add_link.set()

    if message.text == LinkType.TWITTER:
        await bot.send_message(message.from_user.id, enums.TextEnum.LINK_TWITTER,
                               reply_markup=keyboards.Btn_controller.list_btn_req)
        async with state.proxy() as data:
            data['type'] = message.text
        await state_m.Add_information.add_link.set()

    if message.text == LinkType.INSTAGRAM:
        await bot.send_message(message.from_user.id, enums.TextEnum.LINK_INSTAGRAM,
                               reply_markup=keyboards.Btn_controller.list_btn_req)
        async with state.proxy() as data:
            data['type'] = message.text
        await state_m.Add_information.add_link.set()

    if message.text == 'Інше':
        await bot.send_message(message.from_user.id, enums.TextEnum.LINK_ANOTHER,
                               reply_markup=keyboards.Btn_controller.list_btn_req)
        async with state.proxy() as data:
            data['type'] = LinkType.OTHER
        await state_m.Add_information.add_link.set()

    if message.text == keyboards.Btn_text_menu.MENU:
        await bot.send_message(
            message.from_user.id,
            enums.TextEnum.TO_HOMEPAGE,
            reply_markup=keyboards.Btn_main_menu.list_btn
        )
        await state.finish()


@dp.message_handler(state=state_m.Add_information.add_link)
@dp.throttled(anti_flood, rate=1)
async def add_type_link(message: types.Message, state: FSMContext):
    async def type_link(*args: str):
        if args.__len__() == 3:

            if message.text.strip().startswith(args[0]) \
                    or message.text.strip().startswith(args[1]) \
                    or message.text.startswith(args[2]):

                async with state.proxy() as data_links:
                    data_links['link'] = message.text

                await bot.send_message(message.from_user.id, enums.TextEnum.LINK_DESCRIPTION,
                                       reply_markup=keyboards.Btn_controller.list_btn)

                await state_m.Add_information.add_description.set()

            else:
                await bot.send_message(message.from_user.id, enums.TextEnum.WRONG_FORMAT,
                                       reply_markup=keyboards.Btn_controller.list_btn_req)

        if args.__len__() == 2:
            if message.text.strip().startswith(args[0]) or message.text.strip().startswith(args[1]):
                async with state.proxy() as data_links:
                    data_links['link'] = message.text
                await bot.send_message(message.from_user.id, enums.TextEnum.LINK_DESCRIPTION,
                                       reply_markup=keyboards.Btn_controller.list_btn)
                await state_m.Add_information.add_description.set()
            else:
                await bot.send_message(message.from_user.id, enums.TextEnum.WRONG_FORMAT,
                                       reply_markup=keyboards.Btn_controller.list_btn_req)

    if message.text == keyboards.Btn_text_menu.MENU:
        await bot.send_message(message.from_user.id, enums.TextEnum.TO_HOMEPAGE,
                               reply_markup=keyboards.Btn_main_menu.list_btn)
        await state.finish()

    async with state.proxy() as data:

        if data.get('type') != LinkType.TELEGRAM:
            pass
        if data.get('type') == LinkType.TELEGRAM:
            await type_link('https://t.me/', 't.me/')

        if data.get('type') != LinkType.OTHER:
            pass
        else:
            await type_link('https://', 'http://')

        if data.get('type') != LinkType.YOUTUBE:
            pass
        else:
            await type_link('https://www.youtube.com/', 'https://youtube.com', 'https://youtu.be/')

        if data.get('type') != LinkType.FACEBOOK:
            pass
        else:
            await type_link('https://www.facebook.com/', 'https://facebook.com/')

        if data.get('type') != LinkType.TWITTER:
            pass
        else:
            await type_link('https://www.twitter.com/', 'https://twitter.com/')

        if data.get('type') != LinkType.TIKTOK:
            pass
        else:
            await type_link('https://www.tiktok.com/', 'https://tiktok.com/', 'https://vm.tiktok.com/')

        if data.get('type') != LinkType.INSTAGRAM:
            return
        await type_link('https://www.instagram.com/', 'https://instagram.com/')


@dp.message_handler(state=state_m.Add_information.add_description)
@dp.throttled(anti_flood, rate=1)
async def add_descriptions(message: types.Message, state: FSMContext):
    if message.text == keyboards.Btn_text_menu.MENU:
        await bot.send_message(message.from_user.id, enums.TextEnum.TO_HOMEPAGE,
                               reply_markup=keyboards.Btn_main_menu.list_btn)
        await state.finish()

    if message.text == keyboards.Btn_text_controller_inf.SKIP:
        await bot.send_message(message.from_user.id, enums.TextEnum.SKIPPED,
                               reply_markup=keyboards.Btn_main_menu.list_btn)
        async with state.proxy() as data:
            if data.get('type') == LinkType.TELEGRAM:
                if data.get('link').startswith('@'):
                    data['link'] = 't.me/' + data.get('link').replace('@', '')
            check_link = await api_storage_module.create_link(
                link=CreateLinkSchema(
                    link=data.get('link'),
                    link_type=LinkType(data.get('type')),
                    client=message.from_user.id
                )
            )
            if type(check_link) == Exception:
                await bot.send_message(
                    message.from_user.id,
                    enums.TextEnum.LINK_EXISTS,
                    reply_markup=keyboards.Btn_main_menu.list_btn
                )
        await state.finish()

    if message.text != keyboards.Btn_text_menu.MENU and message.text != keyboards.Btn_text_controller_inf.SKIP:
        await bot.send_message(
            message.from_user.id,
            enums.TextEnum.ADDED,
            reply_markup=keyboards.Btn_main_menu.list_btn
        )
        async with state.proxy() as data:
            data['description'] = message.text
        if data.get('type') == LinkType.TELEGRAM:
            if data.get('link').startswith('@'):
                data['link'] = 't.me/' + data.get('link').replace('@', '')

        check_link = await api_storage_module.create_link(
            link=CreateLinkSchema(
                link=data['link'],
                link_type=LinkType(data.get('type')),
                description=data.get('description')
            )
        )
        if type(check_link) == Exception:
            await bot.send_message(
                message.from_user.id,
                enums.TextEnum.LINK_EXISTS,
                reply_markup=keyboards.Btn_main_menu.list_btn
            )
        await state.finish()

