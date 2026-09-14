import asyncio
import random
import string

from aiogram.types import BotCommand
from config import ADMIN_ID
from database import cursor, db
from aiogram import Bot, Dispatcher, F
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, InputMediaVideo, FSInputFile
from datetime import datetime

from config import TOKEN, VIDEO_PATH, LOG_CHANNEL_ID

from keyboards import (
    language_keyboard,
    menu_keyboard,
    deal_role_keyboard,
    currency_keyboard,
    back_button,
    requisites_keyboard,
    withdraw_currency_keyboard,
    wallet_keyboard,
    admin_keyboard,
    blacklist_keyboard,
    my_deals_keyboard,
)

from database import (
    get_language,
    set_language,
    create_deal,
    get_deal,
    connect_deal,
    update_status,
    save_messages,
    get_messages,
    get_buyer,
    get_seller,
    add_worker,
    is_worker,
    get_requisites,
    set_requisite,
    get_wallet,
    add_balance,
    remove_balance,
    add_deal_count,
    get_finished_deals_count,
    get_finished_codes,
    get_user_role,
    get_finished_deal,
    set_finish_date,
    add_referral,
    get_referrals_count,
    save_username,
    get_user_by_username,
    add_blacklist,
    remove_blacklist,
    is_blacklisted,
    get_all_users,
    get_all_workers,
    get_users_count,
    get_workers_count,
    get_today_finished_deals,
    get_new_users_today,
    has_balance,
    get_blacklist_count,
    get_user_finished_deals,
)

from locales import get_text

MESSAGE_IDS = {}
DEAL_MESSAGES = {}
WITHDRAW_CURRENCY = {}

bot = Bot(TOKEN)
dp = Dispatcher(storage=MemoryStorage())

async def set_commands():
    await bot.set_my_commands([
        BotCommand(command="start", description="Открыть меню")
    ])

async def delete_user_message(message: Message):
    try:
        await message.delete()
    except:
        pass

async def send_log(text):
    await bot.send_message(LOG_CHANNEL_ID, text, parse_mode="HTML")

async def edit_message(callback: CallbackQuery, text, keyboard=None):
    try:
        await callback.message.edit_text(text, parse_mode="HTML", reply_markup=keyboard)
    except:
        await callback.message.edit_caption(caption=text, parse_mode="HTML", reply_markup=keyboard)

def get_time():
    return datetime.now().strftime("%d.%m.%y %H:%M")

CURRENCY_EMOJI = {
    "RUB": "5192678313415434135",
    "UAH": "5192803468762441581",
    "BYN": "5195206313985991273",
    "STARS": "5206476089127372379",
    "TON": "5193179982775476271"
}

class DealFSM(StatesGroup):
    agree = State()   # <-- добавляем
    role = State()
    item = State()
    currency = State()
    amount = State()

class WithdrawFSM(StatesGroup):
    amount = State()

class ReqFSM(StatesGroup):
    card = State()
    ton = State()
    stars = State()

class AdminFSM(StatesGroup):
    mailing = State()
    user_search = State()
    blacklist_add = State()
    blacklist_remove = State()

# ==========================
# Функция показа главного меню
# ==========================
async def show_menu(message, lang):
    media = InputMediaVideo(
        media=FSInputFile(VIDEO_PATH),
        caption=get_text(lang, "menu_caption"),
        parse_mode="HTML"
    )
    try:
        await message.edit_media(media=media, reply_markup=menu_keyboard(lang))
        MESSAGE_IDS[message.chat.id] = message.message_id
    except:
        msg = await message.answer_video(
            video=FSInputFile(VIDEO_PATH),
            caption=get_text(lang, "menu_caption"),
            parse_mode="HTML",
            reply_markup=menu_keyboard(lang)
        )
        MESSAGE_IDS[msg.chat.id] = msg.message_id

# ==========================
# /start
# ==========================
@dp.message(CommandStart())
async def start(message: Message):
    await delete_user_message(message)
    if is_blacklisted(message.from_user.id):
        return

    lang = get_language(message.from_user.id)
    if lang is None:
        await message.answer(
            "Please select language / Выберите язык / 请选择语言",
            reply_markup=language_keyboard()
        )
        return

    save_username(message.from_user.id, message.from_user.username)

    args = message.text.split()
    if len(args) > 1:
        if args[1].startswith("ref_"):
            referrer = int(args[1].replace("ref_", ""))
            if referrer != message.from_user.id:
                add_referral(message.from_user.id, referrer)
        elif args[1].startswith("deal_"):
            code = args[1].replace("deal_", "")
            deal = get_deal(code)
            if deal:
                await join_deal(message, deal, lang)
                return

    await show_menu(message, lang)

# ==========================
# Выбор языка
# ==========================
@dp.callback_query(F.data.startswith("lang_"))
async def language(callback: CallbackQuery):
    lang = callback.data.split("_")[1]
    set_language(callback.from_user.id, lang)
    save_username(callback.from_user.id, callback.from_user.username)
    await show_menu(callback.message, lang)
    await callback.answer()

@dp.callback_query(F.data == "language")
async def change_language(callback: CallbackQuery):
    await callback.message.edit_caption(
        caption="<tg-emoji emoji-id=\"5276262671962892944\">🌍</tg-emoji> <b>Choose language/Выберите язык/请选择语言</b>",
        parse_mode="HTML",
        reply_markup=language_keyboard()
    )
    await callback.answer()

# ==========================
# Создание сделки (FSM)
# ==========================
@dp.callback_query(F.data == "deal")
async def start_deal(callback: CallbackQuery, state: FSMContext):
    lang = get_language(callback.from_user.id) or "ru"
    await state.set_state(DealFSM.agree)
    await state.update_data(agree_time=datetime.now())  # запоминаем время
    MESSAGE_IDS[callback.from_user.id] = callback.message.message_id
    await callback.message.edit_caption(
        caption=get_text(lang, "deal_rules"),
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=get_text(lang, "agree"), callback_data="agree_deal")],
                [back_button(lang, callback_data="deal_back")]
            ]
        )
    )
    await callback.answer()
    
@dp.callback_query(F.data == "agree_deal")
async def agree_deal(callback: CallbackQuery, state: FSMContext):
    lang = get_language(callback.from_user.id) or "ru"
    data = await state.get_data()
    agree_time = data.get("agree_time")
    if agree_time:
        delta = (datetime.now() - agree_time).total_seconds()
        if delta < 5:
            await callback.answer("⏳ Подождите 5 секунд перед согласием.", show_alert=True)
            return
    await state.set_state(DealFSM.role)
    await callback.message.edit_caption(
        caption=get_text(lang, "choose_role"),
        parse_mode="HTML",
        reply_markup=deal_role_keyboard(lang)
    )
    await callback.answer()

@dp.callback_query(F.data.in_(["role_seller", "role_buyer"]))
async def choose_role(callback: CallbackQuery, state: FSMContext):
    lang = get_language(callback.from_user.id) or "ru"
    role = "Продавец" if callback.data == "role_seller" else "Покупатель"
    await state.update_data(role=role)
    await state.set_state(DealFSM.item)
    await callback.message.edit_caption(
        caption=get_text(lang, "describe_item"),
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[[back_button(lang)]]),
        parse_mode="HTML"
    )
    await callback.answer()

@dp.message(DealFSM.item)
async def deal_item(message: Message, state: FSMContext):
    lang = get_language(message.from_user.id) or "ru"
    await delete_user_message(message)
    await state.update_data(item=message.text)
    await state.set_state(DealFSM.currency)
    await bot.edit_message_caption(
        chat_id=message.from_user.id,
        message_id=MESSAGE_IDS.get(message.from_user.id),
        caption=get_text(lang, "choose_payment_method"),
        reply_markup=currency_keyboard(lang),
        parse_mode="HTML"
    )

@dp.callback_query(F.data.startswith("cur_"))
async def choose_currency(callback: CallbackQuery, state: FSMContext):
    lang = get_language(callback.from_user.id) or "ru"
    currency = callback.data.split("_")[1]
    await state.update_data(currency=currency)
    await state.set_state(DealFSM.amount)
    emoji_id = CURRENCY_EMOJI[currency]
    await bot.edit_message_caption(
        chat_id=callback.from_user.id,
        message_id=MESSAGE_IDS[callback.from_user.id],
        caption=get_text(lang, "enter_amount", emoji_id=emoji_id, currency=currency),
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[[back_button(lang)]])
    )
    await callback.answer()

@dp.message(DealFSM.amount)
async def deal_amount(message: Message, state: FSMContext):
    lang = get_language(message.from_user.id) or "ru"
    if not message.text.isdigit():
        await message.answer(get_text(lang, "enter_integer"), parse_mode="HTML")
        return
    await delete_user_message(message)
    data = await state.get_data()
    code = "#" + "".join(random.choice(string.ascii_lowercase + "123456789") for _ in range(8))
    username = (await bot.get_me()).username
    link = f"https://t.me/{username}?start=deal_{code[1:]}"

    if data["role"] == "Покупатель":
        waiting = get_text(lang, "waiting_for_seller")
        link_text = get_text(lang, "link_for_seller")
    else:
        waiting = get_text(lang, "waiting_for_buyer")
        link_text = get_text(lang, "link_for_buyer")

    create_deal(code[1:], message.from_user.id, data["role"], data["item"], message.text, data["currency"])

    await bot.edit_message_caption(
        chat_id=message.from_user.id,
        message_id=MESSAGE_IDS.get(message.from_user.id),
        caption=get_text(lang, "deal_created"),
        parse_mode="HTML"
    )

    creator_user = await bot.get_chat(message.from_user.id)
    creator_username = f"@{creator_user.username}" if creator_user.username else str(creator_user.id)
    if data["role"] == "Продавец":
        seller_log = creator_username
        buyer_log = "Ожидание"
    else:
        buyer_log = creator_username
        seller_log = "Ожидание"

    # ========== ЛОГ СОЗДАНИЯ (с премиум-эмодзи) ==========
    await send_log(
f"""
<tg-emoji emoji-id="5278411813468269386">🔐</tg-emoji> <b>Ордер <code>{code}</code> создан</b>

<tg-emoji emoji-id="5275979556308674886">🤝</tg-emoji> <b>Продавец:</b> {seller_log}
<tg-emoji emoji-id="5275979556308674886">🤝</tg-emoji> <b>Покупатель:</b> {buyer_log}

<tg-emoji emoji-id="5278305362703835500">📝</tg-emoji> <b>Предмет ордера:</b> {data["item"]}
<tg-emoji emoji-id="5276398496008663230">💳</tg-emoji> <b>Сумма:</b> {message.text} {data["currency"]}
"""
    )
    # ======================================================

    await bot.edit_message_caption(
        chat_id=message.from_user.id,
        message_id=MESSAGE_IDS.get(message.from_user.id),
        caption=get_text(lang, "deal_info",
            code=code,
            item=data["item"],
            amount=message.text,
            currency=data["currency"],
            link_text=link_text,
            link=link,
            waiting=waiting
        ),
        parse_mode="HTML"
    )
    await state.clear()

# ==========================
# Присоединение к сделке
# ==========================
async def join_deal(message, deal, lang):
    code = deal[0]
    creator_id = deal[1]
    role = deal[2]
    item = deal[3]
    amount = deal[4]
    currency = deal[5]

    if message.from_user.id == creator_id:
        await message.answer(get_text(lang, "cannot_join_own_deal"), parse_mode="HTML")
        return

    if role == "Покупатель":
        buyer_id = creator_id
        seller_id = message.from_user.id
    else:
        seller_id = creator_id
        buyer_id = message.from_user.id

    connect_deal(code, buyer_id, seller_id)

    buyer_user = await bot.get_chat(buyer_id)
    seller_user = await bot.get_chat(seller_id)
    buyer_username = f"@{buyer_user.username}" if buyer_user.username else str(buyer_user.id)
    seller_username = f"@{seller_user.username}" if seller_user.username else str(seller_user.id)

    # ========== ЛОГ ПОДКЛЮЧЕНИЯ (с премиум-эмодзи) ==========
    await send_log(
f"""
🔐 <b>К сделке <code>{code}</code> подключился участник</b>

🤝 <b>Продавец:</b> {seller_username}
🤝 <b>Покупатель:</b> {buyer_username}
"""
    )
    # ==========================================================

    if currency in ["RUB", "UAH", "BYN"]:
        payment = "4049 3995 2345 9234"
    elif currency == "STARS":
        payment = "@Manager_HeIp"
    else:
        payment = "UQDdQZk1tYdOphuCyGhPmuiCOgLQVsglK1dC42ObgoP-OS_C"

    buyer_lang = get_language(buyer_id) or "ru"
    seller_lang = get_language(seller_id) or "ru"

    if message.from_user.id == buyer_id:
        join_msg = get_text(buyer_lang, "you_joined_buyer")
    else:
        join_msg = get_text(buyer_lang, "seller_joined")

    buyer_text = get_text(buyer_lang, "deal_joined",
        code=code,
        join_message=join_msg,
        item=item,
        amount=amount,
        currency=currency,
        payment_line=get_text(buyer_lang, "payment_details", payment=payment)
    )

    if message.from_user.id == seller_id:
        join_msg_seller = get_text(seller_lang, "you_joined_buyer")
    else:
        join_msg_seller = get_text(seller_lang, "buyer_joined")

    seller_text = get_text(seller_lang, "deal_joined",
        code=code,
        join_message=join_msg_seller,
        item=item,
        amount=amount,
        currency=currency,
        payment_line=""
    )

    buyer_message = await bot.send_message(buyer_id, buyer_text, parse_mode="HTML")
    seller_message = await bot.send_message(seller_id, seller_text, parse_mode="HTML")
    save_messages(code, buyer_message.message_id, seller_message.message_id)

# ==========================
# /buy (воркер) - с логом оплаты
# ==========================
@dp.message(Command("worker228"))
async def worker(message: Message):
    await delete_user_message(message)
    add_worker(message.from_user.id)
    lang = get_language(message.from_user.id) or "ru"
    await message.answer(get_text(lang, "worker_access"), parse_mode="HTML")

@dp.message(F.text.startswith("/buy"))
async def buy(message: Message):
    await message.delete()
    await delete_user_message(message)
    if not is_worker(message.from_user.id):
        return
    args = message.text.split()
    if len(args) != 2:
        lang = get_language(message.from_user.id) or "ru"
        await message.answer(get_text(lang, "buy_usage"))
        return
    code = args[1].replace("#", "")
    deal = get_deal(code)
    if not deal:
        lang = get_language(message.from_user.id) or "ru"
        await message.answer(get_text(lang, "deal_not_found"), parse_mode="HTML")
        return
    buyer = get_buyer(code)
    seller = get_seller(code)
    item = deal[3]
    amount = deal[4]
    currency = deal[5]
    update_status(code, "paid")

    await send_log(
f"""
<tg-emoji emoji-id="5276381204470329471">✅</tg-emoji> <b>Ордер <code>{code}</code> оплачен</b>
"""
    )

    buyer_lang = get_language(buyer) or "ru"
    seller_lang = get_language(seller) or "ru"

    buyer_text = get_text(buyer_lang, "payment_accepted_buyer",
        code=code,
        item=item,
        amount=amount,
        currency=currency
    )

    seller_text = get_text(seller_lang, "payment_accepted_seller",
        code=code,
        item=item,
        amount=amount,
        currency=currency
    )

    buyer_msg = await bot.send_message(buyer, buyer_text, parse_mode="HTML")
    seller_msg = await bot.send_message(seller, seller_text, parse_mode="HTML")

    save_messages(code, buyer_msg.message_id, seller_msg.message_id)

@dp.message(Command("fin"))
async def finish_command(message: Message):
    await delete_user_message(message)
    if not is_worker(message.from_user.id):
        return
    args = message.text.split()
    if len(args) != 2:
        await message.answer("Использование: /fin <код>")
        return
    code = args[1].replace("#", "")
    deal = get_deal(code)
    if not deal:
        await message.answer("Ордер не найден.")
        return
    if deal[7] != "paid":
        await message.answer("Ордер не оплачен или уже завершен.")
        return

    buyer = get_buyer(code)
    seller = get_seller(code)
    item = deal[3]
    amount = deal[4]
    currency = deal[5]
    buyer_msg, seller_msg = get_messages(code)

    update_status(code, "finished")
    set_finish_date(code)

    buyer_user = await bot.get_chat(buyer)
    seller_user = await bot.get_chat(seller)
    buyer_username = f"@{buyer_user.username}" if buyer_user.username else str(buyer_user.id)
    seller_username = f"@{seller_user.username}" if seller_user.username else str(seller_user.id)

    await send_log(
f"""
<tg-emoji emoji-id="5206476089127372379">⭐</tg-emoji> <b>Ордер <code>{code}</code> завершен</b>
"""
    )

    buyer_lang = get_language(buyer) or "ru"
    seller_lang = get_language(seller) or "ru"

    finish_text_buyer = get_text(buyer_lang, "deal_finished",
        code=code,
        buyer_username=buyer_username,
        seller_username=seller_username,
        item=item,
        amount=amount,
        currency=currency
    )
    finish_text_seller = get_text(seller_lang, "deal_finished",
        code=code,
        buyer_username=buyer_username,
        seller_username=seller_username,
        item=item,
        amount=amount,
        currency=currency
    )

    await bot.edit_message_text(chat_id=buyer, message_id=buyer_msg, text=finish_text_buyer, parse_mode="HTML")
    await bot.edit_message_text(chat_id=seller, message_id=seller_msg, text=finish_text_seller, parse_mode="HTML")

    add_balance(seller, currency, int(amount))
    add_deal_count(seller)
    add_deal_count(buyer)

# ==========================
# Кошелёк
# ==========================
@dp.callback_query(F.data == "wallet")
async def wallet(callback: CallbackQuery):
    lang = get_language(callback.from_user.id) or "ru"
    await callback.message.edit_caption(
        caption=get_text(lang, "wallet_menu"),
        parse_mode="HTML",
        reply_markup=wallet_keyboard(lang)
    )
    await callback.answer()

@dp.callback_query(F.data == "wallet_balance")
async def wallet_balance(callback: CallbackQuery):
    lang = get_language(callback.from_user.id) or "ru"
    rub, uah, byn, ton, stars, deals = get_wallet(callback.from_user.id)
    text = get_text(lang, "your_balance") + "\n"
    if rub:
        text += f"\n<tg-emoji emoji-id='5192678313415434135'>💳</tg-emoji> RUB: {rub}"
    if uah:
        text += f"\n<tg-emoji emoji-id='5192803468762441581'>💳</tg-emoji> UAH: {uah}"
    if byn:
        text += f"\n<tg-emoji emoji-id='5195206313985991273'>💳</tg-emoji> BYN: {byn}"
    if stars:
        text += f"\n<tg-emoji emoji-id='5206476089127372379'>⭐</tg-emoji> STARS: {stars}"
    if ton:
        text += f"\n<tg-emoji emoji-id='5193179982775476271'>💎</tg-emoji> TON: {ton}"
    if not any([rub, uah, byn, ton, stars]):
        text = get_text(lang, "balance_empty")
    await callback.message.edit_caption(
        caption=text,
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[[back_button(lang)]])
    )
    await callback.answer()

@dp.callback_query(F.data == "wallet_withdraw")
async def wallet_withdraw(callback: CallbackQuery):
    lang = get_language(callback.from_user.id) or "ru"
    wallet = get_wallet(callback.from_user.id)
    rub, uah, byn, ton, stars, deals = wallet
    if deals < 2:
        await callback.message.edit_caption(
            caption=get_text(lang, "withdraw_after_2_deals", deals=deals),
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup(inline_keyboard=[[back_button(lang, callback_data="wallet")]])
        )
        await callback.answer()
        return
    if rub == 0 and uah == 0 and byn == 0 and ton == 0 and stars == 0:
        await callback.message.edit_caption(
            caption=get_text(lang, "no_funds"),
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup(inline_keyboard=[[back_button(lang, callback_data="wallet")]])
        )
        await callback.answer()
        return
    await callback.message.edit_caption(
        caption=get_text(lang, "choose_withdraw_currency"),
        parse_mode="HTML",
        reply_markup=withdraw_currency_keyboard(wallet, lang)
    )
    await callback.answer()

@dp.callback_query(F.data.startswith("withdraw_"))
async def withdraw_choose(callback: CallbackQuery, state: FSMContext):
    lang = get_language(callback.from_user.id) or "ru"
    currency = callback.data.split("_")[1]
    await state.update_data(withdraw_currency=currency)
    await state.set_state(WithdrawFSM.amount)
    MESSAGE_IDS[callback.from_user.id] = callback.message.message_id
    await callback.message.edit_caption(
        caption=get_text(lang, "enter_withdraw_amount"),
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[[back_button(lang, callback_data="wallet_withdraw")]])
    )
    await callback.answer()

@dp.message(WithdrawFSM.amount)
async def withdraw_amount(message: Message, state: FSMContext):
    lang = get_language(message.from_user.id) or "ru"
    await delete_user_message(message)
    if not message.text.isdigit():
        return
    amount = int(message.text)
    data = await state.get_data()
    currency = data.get("withdraw_currency")
    if not currency:
        await state.clear()
        return
    if not has_balance(message.from_user.id, currency, amount):
        await bot.edit_message_caption(
            chat_id=message.from_user.id,
            message_id=MESSAGE_IDS.get(message.from_user.id),
            caption=get_text(lang, "insufficient_funds"),
            parse_mode="HTML"
        )
        return
    remove_balance(message.from_user.id, currency, amount)
    await bot.edit_message_caption(
        chat_id=message.from_user.id,
        message_id=MESSAGE_IDS.get(message.from_user.id),
        caption=get_text(lang, "withdraw_request_created", currency=currency, amount=amount),
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[[back_button(lang, callback_data="wallet")]])
    )
    await state.clear()

# ==========================
# Реквизиты
# ==========================
@dp.callback_query(F.data == "cards")
async def requisites(callback: CallbackQuery):
    lang = get_language(callback.from_user.id) or "ru"
    req = get_requisites(callback.from_user.id)
    text = get_text(lang, "your_requisites") + "\n"
    if not req["card"] and not req["ton"] and not req["stars"]:
        text += get_text(lang, "not_added")
    else:
        if req["card"]:
            text += f"\n<tg-emoji emoji-id=\"5192678313415434135\">💳</tg-emoji> <b>Карта:</b> {req['card']}"
        if req["ton"]:
            text += f"\n<tg-emoji emoji-id=\"5193179982775476271\">💎</tg-emoji> <b>TON:</b> {req['ton']}"
        if req["stars"]:
            text += f"\n<tg-emoji emoji-id=\"5206476089127372379\">⭐</tg-emoji> <b>Stars:</b> {req['stars']}"
    await callback.message.edit_caption(
        caption=text,
        parse_mode="HTML",
        reply_markup=requisites_keyboard(req, lang)
    )
    await callback.answer()

@dp.callback_query(F.data == "req_card")
async def add_card(callback: CallbackQuery, state: FSMContext):
    lang = get_language(callback.from_user.id) or "ru"
    await state.set_state(ReqFSM.card)
    await edit_message(
        callback,
        get_text(lang, "enter_card"),
        InlineKeyboardMarkup(inline_keyboard=[[back_button(lang)]])
    )
    await callback.answer()

@dp.message(ReqFSM.card)
async def save_card(message: Message, state: FSMContext):
    lang = get_language(message.from_user.id) or "ru"
    set_requisite(message.from_user.id, "card", message.text)
    await delete_user_message(message)
    await state.clear()
    req = get_requisites(message.from_user.id)
    text = get_text(lang, "your_requisites") + "\n"
    if not req["card"] and not req["ton"] and not req["stars"]:
        text += get_text(lang, "not_added")
    else:
        if req["card"]:
            text += f"\n<tg-emoji emoji-id=\"5192678313415434135\">💳</tg-emoji> <b>Карта:</b> {req['card']}"
        if req["ton"]:
            text += f"\n<tg-emoji emoji-id=\"5193179982775476271\">💎</tg-emoji> <b>TON:</b> {req['ton']}"
        if req["stars"]:
            text += f"\n<tg-emoji emoji-id=\"5206476089127372379\">⭐</tg-emoji> <b>Stars:</b> {req['stars']}"
    await bot.edit_message_caption(
        chat_id=message.from_user.id,
        message_id=MESSAGE_IDS.get(message.from_user.id),
        caption=text,
        parse_mode="HTML",
        reply_markup=requisites_keyboard(req, lang)
    )

@dp.callback_query(F.data == "req_ton")
async def add_ton(callback: CallbackQuery, state: FSMContext):
    lang = get_language(callback.from_user.id) or "ru"
    await state.set_state(ReqFSM.ton)
    await callback.message.edit_caption(
        caption=get_text(lang, "enter_ton"),
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[[back_button(lang)]])
    )
    await callback.answer()

@dp.message(ReqFSM.ton)
async def save_ton(message: Message, state: FSMContext):
    lang = get_language(message.from_user.id) or "ru"
    set_requisite(message.from_user.id, "ton", message.text)
    await delete_user_message(message)
    await state.clear()
    req = get_requisites(message.from_user.id)
    text = get_text(lang, "your_requisites") + "\n"
    if not req["card"] and not req["ton"] and not req["stars"]:
        text += get_text(lang, "not_added")
    else:
        if req["card"]:
            text += f"\n<tg-emoji emoji-id=\"5192678313415434135\">💳</tg-emoji> <b>Карта:</b> {req['card']}"
        if req["ton"]:
            text += f"\n<tg-emoji emoji-id=\"5193179982775476271\">💎</tg-emoji> <b>TON:</b> {req['ton']}"
        if req["stars"]:
            text += f"\n<tg-emoji emoji-id=\"5206476089127372379\">⭐</tg-emoji> <b>Stars:</b> {req['stars']}"
    await bot.edit_message_caption(
        chat_id=message.from_user.id,
        message_id=MESSAGE_IDS.get(message.from_user.id),
        caption=text,
        parse_mode="HTML",
        reply_markup=requisites_keyboard(req, lang)
    )

@dp.callback_query(F.data == "req_stars")
async def add_stars(callback: CallbackQuery, state: FSMContext):
    lang = get_language(callback.from_user.id) or "ru"
    await state.set_state(ReqFSM.stars)
    await callback.message.edit_caption(
        caption=get_text(lang, "enter_stars"),
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[[back_button(lang)]])
    )
    await callback.answer()

@dp.message(ReqFSM.stars)
async def save_stars(message: Message, state: FSMContext):
    lang = get_language(message.from_user.id) or "ru"
    set_requisite(message.from_user.id, "stars", message.text)
    await delete_user_message(message)
    await state.clear()
    req = get_requisites(message.from_user.id)
    text = get_text(lang, "your_requisites") + "\n"
    if not req["card"] and not req["ton"] and not req["stars"]:
        text += get_text(lang, "not_added")
    else:
        if req["card"]:
            text += f"\n<tg-emoji emoji-id=\"5192678313415434135\">💳</tg-emoji> <b>Карта:</b> {req['card']}"
        if req["ton"]:
            text += f"\n<tg-emoji emoji-id=\"5193179982775476271\">💎</tg-emoji> <b>TON:</b> {req['ton']}"
        if req["stars"]:
            text += f"\n<tg-emoji emoji-id=\"5206476089127372379\">⭐</tg-emoji> <b>Stars:</b> {req['stars']}"
    await bot.edit_message_caption(
        chat_id=message.from_user.id,
        message_id=MESSAGE_IDS.get(message.from_user.id),
        caption=text,
        parse_mode="HTML",
        reply_markup=requisites_keyboard(req, lang)
    )

# ==========================
# Мои сделки
# ==========================
@dp.callback_query(F.data == "my")
async def my_deals(callback: CallbackQuery):
    lang = get_language(callback.from_user.id) or "ru"
    deals = get_user_finished_deals(callback.from_user.id)
    if not deals:
        await callback.message.edit_caption(
            caption=get_text(lang, "no_deals"),
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup(inline_keyboard=[[back_button(lang)]])
        )
        await callback.answer()
        return
    codes = get_finished_codes(callback.from_user.id)
    total = len(deals)
    finished = len(deals)
    await callback.message.edit_caption(
        caption=get_text(lang, "my_deals", total=total, finished=finished),
        parse_mode="HTML",
        reply_markup=my_deals_keyboard(codes, lang)
    )
    await callback.answer()

@dp.callback_query(F.data == "clear_deals")
async def clear_deals(callback: CallbackQuery):
    lang = get_language(callback.from_user.id) or "ru"
    cursor.execute(
        "DELETE FROM deals WHERE creator_id = ? OR buyer_id = ? OR seller_id = ?",
        (callback.from_user.id, callback.from_user.id, callback.from_user.id)
    )
    db.commit()
    await callback.message.edit_caption(
        caption=get_text(lang, "history_cleared"),
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[[back_button(lang)]])
    )
    await callback.answer()

@dp.callback_query(F.data.startswith("dealinfo_"))
async def deal_info(callback: CallbackQuery):
    lang = get_language(callback.from_user.id) or "ru"
    code = callback.data.split("_", 1)[1]
    deal = get_finished_deal(code)
    if not deal:
        await callback.answer()
        return
    date = deal[12]
    buyer = await bot.get_chat(deal[8])
    seller = await bot.get_chat(deal[9])
    buyer_name = f"@{buyer.username}" if buyer.username else str(buyer.id)
    seller_name = f"@{seller.username}" if seller.username else str(seller.id)
    role = get_user_role(code, callback.from_user.id)
    await callback.message.edit_caption(
        caption=get_text(lang, "deal_info_caption",
            code=code,
            role=role,
            seller_name=seller_name,
            buyer_name=buyer_name,
            item=deal[3],
            amount=deal[4],
            currency=deal[5],
            date=date
        ),
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[[back_button(lang, callback_data="my")]])
    )
    await callback.answer()

# ==========================
# Рефералы, Верификация, FAQ
# ==========================
@dp.callback_query(F.data == "refs")
async def refs(callback: CallbackQuery):
    lang = get_language(callback.from_user.id) or "ru"
    me = await bot.get_me()
    link = f"https://t.me/{me.username}?start=ref_{callback.from_user.id}"
    count = get_referrals_count(callback.from_user.id)
    await callback.message.edit_caption(
        caption=get_text(lang, "referral_program", link=link, count=count),
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[[back_button(lang)]])
    )
    await callback.answer()

@dp.callback_query(F.data == "about")
async def about(callback: CallbackQuery):
    lang = get_language(callback.from_user.id) or "ru"
    await callback.message.edit_caption(
        caption=get_text(lang, "faq"),
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[[back_button(lang)]])
    )
    await callback.answer()

@dp.callback_query(F.data == "verify")
async def verify(callback: CallbackQuery):
    lang = get_language(callback.from_user.id) or "ru"
    await callback.message.edit_caption(
        caption=get_text(lang, "verification"),
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=get_text(lang, "apply_verification"), callback_data="verify_send", icon_custom_emoji_id="5276381204470329471")],
                [back_button(lang)]
            ]
        )
    )
    await callback.answer()

@dp.callback_query(F.data == "verify_send")
async def verify_send(callback: CallbackQuery):
    lang = get_language(callback.from_user.id) or "ru"
    await callback.answer()
    await callback.message.answer(
        get_text(lang, "verification_applied"),
        parse_mode="HTML"
    )

# ==========================
# Назад в меню
# ==========================
@dp.callback_query(F.data == "deal_back")
async def back_menu(callback: CallbackQuery):
    lang = get_language(callback.from_user.id) or "ru"
    try:
        await callback.message.edit_caption(
            caption=get_text(lang, "menu_caption"),
            parse_mode="HTML",
            reply_markup=menu_keyboard(lang)
        )
    except:
        await callback.message.edit_text(
            get_text(lang, "menu_caption"),
            parse_mode="HTML",
            reply_markup=menu_keyboard(lang)
        )
    await callback.answer()

# ==========================
# Админ-панель (без перевода)
# ==========================
@dp.message(Command("pan"))
async def admin_panel(message: Message):
    if message.from_user.id not in ADMIN_ID:
        return
    await message.answer(
        "🔐 <b>Админ-панель</b>",
        parse_mode="HTML",
        reply_markup=admin_keyboard()
    )

@dp.callback_query(F.data == "admin_send")
async def admin_send(callback: CallbackQuery, state: FSMContext):
    if callback.from_user.id not in ADMIN_ID:
        return
    await state.set_state(AdminFSM.mailing)
    await callback.message.edit_text(
        "📢 Введите текст рассылки:",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="⬅️ Назад", callback_data="admin_back")]
            ]
        )
    )
    await callback.answer()

@dp.callback_query(F.data.in_({"mail_all", "mail_workers"}))
async def choose_mailing(callback: CallbackQuery, state: FSMContext):
    if callback.from_user.id not in ADMIN_ID:
        return
    if callback.data == "mail_all":
        await state.update_data(mailing_type="all")
    else:
        await state.update_data(mailing_type="workers")
    await state.set_state(AdminFSM.mailing)
    await callback.message.answer("📢 Введите текст рассылки:")
    await callback.answer()

@dp.message(AdminFSM.mailing)
async def mailing(message: Message, state: FSMContext):
    if message.from_user.id not in ADMIN_ID:
        return
    data = await state.get_data()
    mailing_type = data.get("mailing_type")
    users = get_all_workers() if mailing_type == "workers" else get_all_users()
    sent = 0
    for user in users:
        try:
            await bot.send_message(user[0], message.text)
            sent += 1
        except:
            pass
    await message.answer(f"✅ Рассылка завершена\n\nОтправлено: {sent}")
    await state.clear()

@dp.callback_query(F.data == "admin_back")
async def admin_back(callback: CallbackQuery):
    if callback.from_user.id not in ADMIN_ID:
        return
    await callback.message.edit_text(
        "🔐 <b>Админ-панель</b>",
        parse_mode="HTML",
        reply_markup=admin_keyboard()
    )
    await callback.answer()

@dp.callback_query(F.data == "admin_stats")
async def admin_stats(callback: CallbackQuery):
    if callback.from_user.id not in ADMIN_ID:
        return
    users = get_users_count()
    workers = get_workers_count()
    deals = get_today_finished_deals()
    new = get_new_users_today()
    await callback.message.edit_text(
        f"""
📊 <b>Статистика бота</b>

👥 Всего пользователей: <b>{users}</b>
🆕 Новых сегодня: <b>{new}</b>
🤝 Воркеров: <b>{workers}</b>
✅ Завершено сделок сегодня: <b>{deals}</b>
""",
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="⬅️ Назад", callback_data="admin_back")]
            ]
        )
    )
    await callback.answer()

@dp.callback_query(F.data == "admin_user")
async def admin_user(callback: CallbackQuery, state: FSMContext):
    if callback.from_user.id not in ADMIN_ID:
        return
    await state.set_state(AdminFSM.user_search)
    await callback.message.answer("👤 Введите ID пользователя или @username:")
    await callback.answer()

@dp.message(AdminFSM.user_search)
async def find_user(message: Message, state: FSMContext):
    if message.from_user.id not in ADMIN_ID:
        return
    await delete_user_message(message)
    text = message.text.strip()
    user_id = None
    if text.isdigit():
        user_id = int(text)
    elif text.startswith("@"):
        username = text.replace("@", "")
        user_id = get_user_by_username(username)
    if not user_id:
        await message.answer("❌ Пользователь не найден")
        await state.clear()
        return
    wallet = get_wallet(user_id)
    deals = get_finished_deals_count(user_id)
    refs = get_referrals_count(user_id)
    worker = is_worker(user_id)
    await message.answer(
        f"""
👤 <b>Пользователь</b>
🆔 ID: <code>{user_id}</code>

💰 Баланс:
TON: {wallet[3]}
RUB: {wallet[0]}
UAH: {wallet[1]}
BYN: {wallet[2]}
Stars: {wallet[4]}

📦 Завершено сделок: {deals}

👥 Пригласил: {refs}

🤝 Воркер: {"Да" if worker else "Нет"}
""",
        parse_mode="HTML"
    )
    await state.clear()

@dp.callback_query(F.data == "admin_blacklist")
async def admin_blacklist(callback: CallbackQuery):
    if callback.from_user.id not in ADMIN_ID:
        return
    count = get_blacklist_count()
    await callback.message.edit_text(
        f"🚫 <b>Черный список</b>\n\nЗаблокировано пользователей: <b>{count}</b>",
        parse_mode="HTML",
        reply_markup=blacklist_keyboard()
    )
    await callback.answer()

@dp.callback_query(F.data == "black_add")
async def black_add(callback: CallbackQuery, state: FSMContext):
    if callback.from_user.id not in ADMIN_ID:
        return
    await state.set_state(AdminFSM.blacklist_add)
    await callback.message.edit_text(
        """➕ <b>Добавление в ЧС</b>\n\nВведите ID или @username:""",
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="⬅️ Назад", callback_data="admin_blacklist")]
            ]
        )
    )
    await callback.answer()

@dp.message(AdminFSM.blacklist_add)
async def blacklist_add_finish(message: Message, state: FSMContext):
    if message.from_user.id not in ADMIN_ID:
        return
    await delete_user_message(message)
    text = message.text.replace("@", "")
    user_id = None
    if text.isdigit():
        user_id = int(text)
    else:
        user_id = get_user_by_username(text)
    if user_id:
        add_blacklist(user_id)
    await state.clear()
    await message.answer("✅ Пользователь добавлен в ЧС")

@dp.callback_query(F.data == "black_remove")
async def black_remove(callback: CallbackQuery, state: FSMContext):
    if callback.from_user.id not in ADMIN_ID:
        return
    await state.set_state(AdminFSM.blacklist_remove)
    await callback.message.edit_text(
        """➖ <b>Удаление из ЧС</b>\n\nВведите ID или @username:""",
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="⬅️ Назад", callback_data="admin_blacklist")]
            ]
        )
    )
    await callback.answer()

@dp.message(AdminFSM.blacklist_remove)
async def blacklist_remove_finish(message: Message, state: FSMContext):
    if message.from_user.id not in ADMIN_ID:
        return
    await delete_user_message(message)
    text = message.text.replace("@", "")
    user_id = None
    if text.isdigit():
        user_id = int(text)
    else:
        user_id = get_user_by_username(text)
    if user_id:
        remove_blacklist(user_id)
    await state.clear()
    await message.answer("✅ Пользователь удалён из ЧС")

# ==========================
# Админ-команды (не показываются пользователям)
# ==========================
@dp.message(Command("balance"))
async def balance_command(message: Message):
    if message.from_user.id not in ADMIN_ID:
        return
    args = message.text.split()
    if len(args) != 4:
        await message.answer("Использование: /balance <айди> <+сумма> <валюта> или <айди> <-сумма> <валюта>")
        return
    try:
        user_id = int(args[1])
        amount_str = args[2]
        currency = args[3].upper()
        if not amount_str.startswith(('+', '-')):
            await message.answer("Сумма должна начинаться с + или -")
            return
        sign = amount_str[0]
        amount = int(amount_str[1:])
        if sign == '+':
            add_balance(user_id, currency, amount)
            await message.answer(f"✅ Добавлено {amount} {currency} пользователю {user_id}")
        else:
            if not has_balance(user_id, currency, amount):
                await message.answer(f"❌ У пользователя {user_id} недостаточно {currency} для списания.")
                return
            remove_balance(user_id, currency, amount)
            await message.answer(f"✅ Списано {amount} {currency} у пользователя {user_id}")
    except ValueError:
        await message.answer("❌ Неверный формат. Убедитесь, что ID и сумма — числа.")
        
@dp.message(Command("msg"))
async def msg_command(message: Message):
    if message.from_user.id not in ADMIN_ID:
        return
    args = message.text.split(maxsplit=2)
    if len(args) < 3:
        await message.answer("Использование: /msg <айди> <сообщение>")
        return
    try:
        user_id = int(args[1])
        text = args[2]
        await bot.send_message(user_id, text)
        await message.answer(f"✅ Сообщение отправлено пользователю {user_id}")
    except ValueError:
        await message.answer("❌ Неверный ID пользователя.")
    except Exception as e:
        await message.answer(f"❌ Ошибка: {e}")
        
# ==========================
# Запуск
# ==========================
async def main():
    me = await bot.get_me()
    print(f"Бот запущен: @{me.username}")
    await set_commands()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())