from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from locales import get_text

EMOJI = {
    "deal": "5278613311858959074",
    "wallet": "5193179982775476271",
    "deals": "5278227821364275264",
    "cards": "5276398496008663230",
    "language": "5276111746812112286",
    "support": "5278528159837348960",
    "verify": "5276262671962892944",
    "refs": "5276422526350681413",
    "about": "5278753302023004775",
}

def language_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🇷🇺 Русский", callback_data="lang_ru")],
            [InlineKeyboardButton(text="🇬🇧 English", callback_data="lang_en")],
            [InlineKeyboardButton(text="🇨🇳 中文", callback_data="lang_cn")],
        ]
    )

def btn(text, callback, emoji):
    return InlineKeyboardButton(
        text=text,
        callback_data=callback,
        icon_custom_emoji_id=emoji
    )

def back_button(lang, text=None, callback_data="deal_back"):
    if text is None:
        text = get_text(lang, "back")
    return InlineKeyboardButton(
        text=text,
        callback_data=callback_data,
        icon_custom_emoji_id="5206510891247371052"
    )

def deal_role_keyboard(lang):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=get_text(lang, "role_seller"),
                    callback_data="role_seller",
                    icon_custom_emoji_id="5275979556308674886"
                )
            ],
            [
                InlineKeyboardButton(
                    text=get_text(lang, "role_buyer"),
                    callback_data="role_buyer",
                    icon_custom_emoji_id="5275979556308674886"
                )
            ],
            [
                back_button(lang)
            ]
        ]
    )

def currency_keyboard(lang):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="RUB", callback_data="cur_RUB", icon_custom_emoji_id="5192678313415434135")],
            [InlineKeyboardButton(text="UAH", callback_data="cur_UAH", icon_custom_emoji_id="5192803468762441581")],
            [InlineKeyboardButton(text="BYN", callback_data="cur_BYN", icon_custom_emoji_id="5195206313985991273")],
            [InlineKeyboardButton(text="STARS", callback_data="cur_STARS", icon_custom_emoji_id="5206476089127372379")],
            [InlineKeyboardButton(text="TON", callback_data="cur_TON", icon_custom_emoji_id="5193179982775476271")],
            [back_button(lang)]
        ]
    )

def menu_keyboard(lang):
    if lang == "ru":
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [btn("Создать ордер", "deal", EMOJI["deal"]), btn("Средства", "wallet", EMOJI["wallet"])],
                [btn("Мои ордера", "my", EMOJI["deals"]), btn("Реквизиты", "cards", EMOJI["cards"])],
                [btn("Язык", "language", EMOJI["language"]),
                 InlineKeyboardButton(text="Поддержка", url="https://t.me/Manager_HeIp", icon_custom_emoji_id=EMOJI["support"])],
                [btn("Верификация", "verify", EMOJI["verify"]), btn("Рефералы", "refs", EMOJI["refs"])],
                [btn("О сервисе", "about", EMOJI["about"])]
            ]
        )
    elif lang == "en":
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [btn("Create order", "deal", EMOJI["deal"]), btn("Wallet", "wallet", EMOJI["wallet"])],
                [btn("My orders", "my", EMOJI["deals"]), btn("Payment", "cards", EMOJI["cards"])],
                [btn("Language", "language", EMOJI["language"]),
                 InlineKeyboardButton(text="Support", url="https://t.me/Manager_HeIp", icon_custom_emoji_id=EMOJI["support"])],
                [btn("Verification", "verify", EMOJI["verify"]), btn("Referrals", "refs", EMOJI["refs"])],
                [btn("About", "about", EMOJI["about"])]
            ]
        )
    else:  # cn
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [btn("创建订单", "deal", EMOJI["deal"]), btn("钱包", "wallet", EMOJI["wallet"])],
                [btn("我的订单", "my", EMOJI["deals"]), btn("收款方式", "cards", EMOJI["cards"])],
                [btn("语言", "language", EMOJI["language"]),
                 InlineKeyboardButton(text="支持", url="https://t.me/Manager_HeIp", icon_custom_emoji_id=EMOJI["support"])],
                [btn("验证", "verify", EMOJI["verify"]), btn("推荐", "refs", EMOJI["refs"])],
                [btn("关于", "about", EMOJI["about"])]
            ]
        )

def requisites_keyboard(req, lang):
    card_text = get_text(lang, "add_card") if not req["card"] else get_text(lang, "change_card")
    ton_text = get_text(lang, "add_ton") if not req["ton"] else get_text(lang, "change_ton")
    stars_text = get_text(lang, "add_stars") if not req["stars"] else get_text(lang, "change_stars")
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=card_text, callback_data="req_card", icon_custom_emoji_id="5192678313415434135")],
            [InlineKeyboardButton(text=ton_text, callback_data="req_ton", icon_custom_emoji_id="5193179982775476271")],
            [InlineKeyboardButton(text=stars_text, callback_data="req_stars", icon_custom_emoji_id="5206476089127372379")],
            [back_button(lang)]
        ]
    )

def wallet_keyboard(lang):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=get_text(lang, "wallet_balance"), callback_data="wallet_balance", icon_custom_emoji_id="5195107400889163662")],
            [InlineKeyboardButton(text=get_text(lang, "withdraw"), callback_data="wallet_withdraw", icon_custom_emoji_id="5276220667182736079")],
            [back_button(lang)]
        ]
    )

def withdraw_currency_keyboard(wallet, lang):
    rub, uah, byn, ton, stars, deals = wallet
    buttons = []
    if rub > 0:
        buttons.append([InlineKeyboardButton(text="RUB", callback_data="withdraw_RUB", icon_custom_emoji_id="5192678313415434135")])
    if uah > 0:
        buttons.append([InlineKeyboardButton(text="UAH", callback_data="withdraw_UAH", icon_custom_emoji_id="5192803468762441581")])
    if byn > 0:
        buttons.append([InlineKeyboardButton(text="BYN", callback_data="withdraw_BYN", icon_custom_emoji_id="5195206313985991273")])
    if stars > 0:
        buttons.append([InlineKeyboardButton(text="STARS", callback_data="withdraw_STARS", icon_custom_emoji_id="5206476089127372379")])
    if ton > 0:
        buttons.append([InlineKeyboardButton(text="TON", callback_data="withdraw_TON", icon_custom_emoji_id="5193179982775476271")])
    buttons.append([back_button(lang, callback_data="wallet_back")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def my_deals_keyboard(codes, lang):
    keyboard = []
    for code in codes:
        keyboard.append([
            InlineKeyboardButton(
                text=get_text(lang, "deal_prefix", code=code),
                callback_data=f"dealinfo_{code}",
                icon_custom_emoji_id="5278753302023004775"
            )
        ])
    keyboard.append([
        InlineKeyboardButton(
            text=get_text(lang, "clear_history"),
            callback_data="clear_deals"
        )
    ])
    keyboard.append([back_button(lang)])
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

# Админские клавиатуры (без перевода, только для админов)
def admin_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📢 Рассылка", callback_data="admin_send")],
            [InlineKeyboardButton(text="👤 Пользователь", callback_data="admin_user")],
            [InlineKeyboardButton(text="📊 Статистика", callback_data="admin_stats")],
            [InlineKeyboardButton(text="🚫 Черный список", callback_data="admin_blacklist")]
        ]
    )

def mailing_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="👥 Всем пользователям", callback_data="mail_all")],
            [InlineKeyboardButton(text="🤝 Только воркерам", callback_data="mail_workers")],
            [InlineKeyboardButton(text="⬅️ Назад", callback_data="admin_back")]
        ]
    )

def workers_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="➕ Добавить воркера", callback_data="add_worker")],
            [InlineKeyboardButton(text="➖ Удалить воркера", callback_data="remove_worker")],
            [InlineKeyboardButton(text="⬅️ Назад", callback_data="admin_back")]
        ]
    )

def blacklist_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="➕ Заблокировать", callback_data="black_add")],
            [InlineKeyboardButton(text="➖ Разблокировать", callback_data="black_remove")],
            [InlineKeyboardButton(text="⬅️ Назад", callback_data="admin_back")]
        ]
    )