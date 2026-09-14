LOCALES = {
    "ru": {
        "choose_language": "Пожалуйста, выберите язык",
        "choose_role": "<tg-emoji emoji-id=\"5275979556308674886\">🤝</tg-emoji> <b>Выберите вашу роль в ордере:</b>",
        "choose_payment_method": "<tg-emoji emoji-id=\"5276398496008663230\">💳</tg-emoji> <b>Выберите способ оплаты</b>",
        "wallet_menu": "<tg-emoji emoji-id=\"5193179982775476271\">💎</tg-emoji> <b>Выберите действие:</b>",
        "history_cleared": "<tg-emoji emoji-id=\"5278578973595427038\">🗑</tg-emoji> <b>История ордеров очищена.</b>",
        "menu_caption": """
<tg-emoji emoji-id="5276262671962892944">🏠</tg-emoji> <b>Laguna Gifts</b>

<tg-emoji emoji-id="5278753302023004775">🛡</tg-emoji> Безопасный гарант для ордеров в Telegram.

<b>Что внутри:</b>

• Защита от мошенников
• Средства удерживаются до закрытия ордера
• История всех ордеров
• Поддержка 24/7

Выберите действие ниже.
""",
        "deal_rules": """
<tg-emoji emoji-id="5278753302023004775">📄</tg-emoji> <b>Правила ордера</b>

1. Ордер считается закрытым, после подтверждения оплаты и передачи товара.
2. Продавец обязуется передать товар в полном объеме на указанные реквизиты.
3. Покупатель обязуется произвести оплату в полном объеме на указанные реквизиты.
4. В случае возникновения спора, администрация обязана принять решение на основе предоставленных доказательств.
5. Запрещены мошеннические действия. При выявлении мошенничества аккаунт блокируется без возможности восстановления.
6. Администрация не несет ответственности за качество передаваемого товара, если иное не оговорено дополнительно.
7. Администрация не несет ответственности за несоблюдение правил ордера покупателем или продавцом.

Нажимая «Принимаю», вы соглашаетесь с правилами ордера.
""",
        "agree": "Принимаю",
        "wait_5_seconds": "⏳ Подождите 5 секунд перед согласием.",
        "describe_item": "<tg-emoji emoji-id=\"5278305362703835500\">📝</tg-emoji> <b>Опишите предмет ордера</b>",
        "enter_amount": "<tg-emoji emoji-id=\"{emoji_id}\">💰</tg-emoji> <b>Введите сумму ордера в {currency}</b>\n\nТолько целое число.",
        "deal_created": "<tg-emoji emoji-id=\"5278411813468269386\">🔐</tg-emoji> <b>Создание ордера...</b>",
        "deal_info": """
<tg-emoji emoji-id="5278411813468269386">🔐</tg-emoji> <b>Ордер</b> <code>{code}</code>

<tg-emoji emoji-id="5278305362703835500">📝</tg-emoji> <b>Предмет ордера:</b> {item}
<tg-emoji emoji-id="5276398496008663230">💳</tg-emoji> <b>Сумма:</b> {amount} {currency}
<tg-emoji emoji-id="5278305362703835500">🔗</tg-emoji> <b>Ссылка для {link_text}:</b> {link}

<tg-emoji emoji-id="5278411813468269386">🔐</tg-emoji> <b>Статус:</b> ожидает {waiting}
""",
        "cannot_join_own_deal": "<tg-emoji emoji-id=\"5278578973595427038\">❌</tg-emoji> <b>Вы не можете подключиться к своему ордеру.</b>",
        "you_joined_buyer": "<tg-emoji emoji-id=\"5278411813468269386\">🔐</tg-emoji> <b>Вы подключились к ордеру</b>",
        "seller_joined": "<tg-emoji emoji-id=\"5278411813468269386\">🔐</tg-emoji> <b>Продавец подключился к ордеру</b>",
        "buyer_joined": "<tg-emoji emoji-id=\"5278411813468269386\">🔐</tg-emoji> <b>Покупатель подключился к ордеру</b>",
        "payment_details": "<tg-emoji emoji-id=\"5276398496008663230\">💳</tg-emoji> <b>Реквизиты для оплаты:</b> {payment}",
        "status_waiting_payment": "<tg-emoji emoji-id=\"5278411813468269386\">🔐</tg-emoji> <b>Статус:</b> ожидает оплаты",
        "deal_joined": """
<tg-emoji emoji-id="5278227821364275264">💼</tg-emoji> <b>Ордер</b> <code>{code}</code>

{join_message}

<tg-emoji emoji-id="5278305362703835500">📝</tg-emoji> <b>Предмет ордера:</b> {item}
<tg-emoji emoji-id="5276398496008663230">💳</tg-emoji> <b>Сумма:</b> {amount} {currency}
{payment_line}
<tg-emoji emoji-id="5278411813468269386">🔐</tg-emoji> <b>Статус:</b> ожидает оплаты
""",
        "payment_accepted_buyer": """
<tg-emoji emoji-id="5278227821364275264">💼</tg-emoji> <b>Ордер</b> <code>{code}</code>

<tg-emoji emoji-id="5278411813468269386">🔐</tg-emoji> <b>Ваша оплата принята</b>

<tg-emoji emoji-id="5278305362703835500">📝</tg-emoji> <b>Предмет ордера:</b> {item}
<tg-emoji emoji-id="5276398496008663230">💳</tg-emoji> <b>Сумма:</b> {amount} {currency}

<tg-emoji emoji-id="5278411813468269386">🔐</tg-emoji> <b>Статус:</b> ожидает передачи товара
""",
        "payment_accepted_seller": """
<tg-emoji emoji-id="5278227821364275264">💼</tg-emoji> <b>Ордер</b> <code>{code}</code>

<tg-emoji emoji-id="5278411813468269386">🔐</tg-emoji> <b>Оплата покупателя принята</b>

<tg-emoji emoji-id="5278305362703835500">📝</tg-emoji> <b>Предмет ордера:</b> {item}
<tg-emoji emoji-id="5276398496008663230">💳</tg-emoji> <b>Сумма:</b> {amount} {currency}
<tg-emoji emoji-id="5276398496008663230">💳</tg-emoji> <b>Реквизиты:</b> Передайте товар менеджеру @Manager_HeIp

<tg-emoji emoji-id="5278411813468269386">🔐</tg-emoji> <b>Статус:</b> ожидает передачи товара
""",
        "seller_sent_goods": "🔐 Продавец передал товар",
        "deal_finished": """
<tg-emoji emoji-id="5278411813468269386">🔐</tg-emoji> <b>Ордер <code>{code}</code> закрыт</b>

<tg-emoji emoji-id="5275979556308674886">🤝</tg-emoji> <b>Покупатель:</b> {buyer_username}
<tg-emoji emoji-id="5275979556308674886">🤝</tg-emoji> <b>Продавец:</b> {seller_username}

<tg-emoji emoji-id="5278305362703835500">📝</tg-emoji> <b>Предмет ордера:</b> {item}
<tg-emoji emoji-id="5276398496008663230">💳</tg-emoji> <b>Сумма:</b> {amount} {currency}
""",
        "your_balance": "<tg-emoji emoji-id=\"5276398496008663230\">💳</tg-emoji> <b>Ваш баланс:</b>",
        "balance_empty": "<tg-emoji emoji-id=\"5278578973595427038\">❌</tg-emoji> <b>Ваш баланс пуст</b>",
        "withdraw_after_2_deals": "<tg-emoji emoji-id=\"5278578973595427038\">❌</tg-emoji> <b>Вывод средств доступен после 2 ордеров.</b>\n\nСейчас у вас: {deals} ордеров",
        "no_funds": "<tg-emoji emoji-id=\"5278578973595427038\">❌</tg-emoji> <b>Нет средств для вывода.</b>",
        "choose_withdraw_currency": "<tg-emoji emoji-id=\"5276220667182736079\">💸</tg-emoji> <b>Выберите валюту, которую хотите вывести.</b>",
        "enter_withdraw_amount": "<tg-emoji emoji-id=\"5276220667182736079\">💸</tg-emoji> <b>Введите сумму, которую хотите вывести</b>\n\nТолько целое число.",
        "insufficient_funds": "<tg-emoji emoji-id=\"5278578973595427038\">❌</tg-emoji> <b>Недостаточно средств.</b>",
        "withdraw_request_created": """
<tg-emoji emoji-id="5278411813468269386">🔐</tg-emoji> <b>Заявка на вывод успешно создана</b>

<b>Валюта:</b> {currency}
<b>Сумма:</b> {amount}

<tg-emoji emoji-id="5278753302023004775">📄</tg-emoji> Ожидайте вывод в течение 5–120 минут.
""",
        "your_requisites": "<tg-emoji emoji-id=\"5276398496008663230\">💳</tg-emoji> <b>Ваши реквизиты:</b>",
        "not_added": "<tg-emoji emoji-id=\"5278578973595427038\">❌</tg-emoji> <b>Не добавлено</b>",
        "add_card": "Добавить карту",
        "change_card": "Изменить карту",
        "add_ton": "Добавить TON кошелек",
        "change_ton": "Изменить TON кошелек",
        "add_stars": "Добавить получателя звезд",
        "change_stars": "Изменить получателя звезд",
        "enter_card": "<tg-emoji emoji-id=\"5276398496008663230\">💳</tg-emoji> <b>Введите номер карты:</b>",
        "enter_ton": "<tg-emoji emoji-id=\"5193179982775476271\">💎</tg-emoji> <b>Введите TON кошелек:</b>",
        "enter_stars": "<tg-emoji emoji-id=\"5206476089127372379\">⭐</tg-emoji> <b>Введите получателя Stars:</b>",
        "no_deals": "<tg-emoji emoji-id=\"5278578973595427038\">❌</tg-emoji> <b>У вас нет ордеров.</b>",
        "my_deals": """
<tg-emoji emoji-id="5278227821364275264">💼</tg-emoji> <b>Мои ордера</b>

<b>Общее количество ордеров:</b> {total}
<b>Закрытые ордера:</b> {finished}

Ниже указаны только закрытые ордера.
""",
        "deal_info_caption": """
<tg-emoji emoji-id="5278753302023004775">📄</tg-emoji> <b>Ордер</b> <code>{code}</code>

<tg-emoji emoji-id="5275979556308674886">🤝</tg-emoji> <b>Ваша роль:</b> {role}
<b>Продавец:</b> {seller_name}
<b>Покупатель:</b> {buyer_name}

<b>Предмет ордера:</b> {item}
<b>Сумма:</b> {amount} {currency}

<tg-emoji emoji-id="5278411813468269386">🔐</tg-emoji> <b>Статус:</b> закрыт

<b>Дата:</b> {date}
""",
        "verification": """
<tg-emoji emoji-id="5276262671962892944">✔️</tg-emoji> <b>Верификация</b>

Верификация доступна пользователям с 20+ успешными ордерами и оборотом от 250 USDT.

<b>Преимущества:</b>
• автовывод средств
• приоритетная поддержка
• ускоренное решение спорных ситуаций

Подайте заявку, и администрация рассмотрит ее.
""",
        "apply_verification": "Подать заявку",
        "verification_applied": """
<tg-emoji emoji-id="5278411813468269386">🔐</tg-emoji> <b>Заявка на верификацию успешно подана</b>

<tg-emoji emoji-id="5278753302023004775">📄</tg-emoji> Ожидайте ответа администрации.

Уведомление о решении вы получите в течение 12–48 часов.
""",
        "referral_program": """
<tg-emoji emoji-id="5276422526350681413">👥</tg-emoji> <b>Реферальная программа</b>

<tg-emoji emoji-id="5278753302023004775">📄</tg-emoji> За каждого приглашенного пользователя вы получаете <b>0.3 TON</b> на баланс бота.

<b>Ваша ссылка:</b> {link}

<b>Приглашено пользователей:</b> {count}
""",
        "faq": """
<tg-emoji emoji-id="5278753302023004775">📄</tg-emoji> <b>F.A.Q - Часто задаваемые вопросы</b>

<b>1. Что делает бот?</b>
<tg-emoji emoji-id="5276127848644503161">📦</tg-emoji> Бот работает как автоматический сервис-гарант: обеспечивает безопасный обмен NFT-подарками, Telegram-каналами, чатами, кодами ботов и другими цифровыми товарами.

<b>2. Что можно купить или продать?</b>
<tg-emoji emoji-id="5278540791336165644">💎</tg-emoji> Почти что угодно — от цифровых активов до кодов, подписок и Telegram-ресурсов.

<b>3. Как работает ордер?</b>
<tg-emoji emoji-id="5206202791768393003">⚙️</tg-emoji> Все транзакции автоматизированы: бот удерживает товар и оплату, затем переводит средства и активы после подтверждения обеими сторонами.

<b>4. Как вывести средства?</b>
<tg-emoji emoji-id="5276398496008663230">💳</tg-emoji> Вывод доступен в любой удобной валюте, от двух сделок.

<b>5. Есть ли поддержка?</b>
<tg-emoji emoji-id="5278528159837348960">🛟</tg-emoji> Да! Поддержка доступна 24/7 и поможет с любыми вопросами.

<b>6. Это безопасно?</b>
<tg-emoji emoji-id="5276262671962892944">✅</tg-emoji> Да, бот использует автоматическую систему гаранта, исключающую риск мошенничества.
""",
        "enter_integer": "<tg-emoji emoji-id=\"5278578973595427038\">❌</tg-emoji> <b>Введите только целое число.</b>",
        "deal_not_found": "<tg-emoji emoji-id=\"5278578973595427038\">❌</tg-emoji> Ордер не найден.",
        "buy_usage": "Использование:\n/buy КОД",
        "worker_access": "<tg-emoji emoji-id=\"5278411813468269386\">🔐</tg-emoji> <b>Вы получили доступ к команде /buy.</b>",
        "back": "Назад",
        "role_seller": "Я продавец",
        "role_buyer": "Я покупатель",
        "wallet_balance": "Посмотреть баланс",
        "withdraw": "Вывести",
        "clear_history": "🗑 Очистить историю",
        "deal_prefix": "Ордер {code}",
        "waiting_for_seller": "продавца",
        "link_for_seller": "продавца",
        "waiting_for_buyer": "покупателя",
        "link_for_buyer": "покупателя",
    },
    "en": {
        "choose_language": "Please select language",
        "choose_role": "<tg-emoji emoji-id=\"5275979556308674886\">🤝</tg-emoji> <b>Choose your role in the order:</b>",
        "choose_payment_method": "<tg-emoji emoji-id=\"5276398496008663230\">💳</tg-emoji> <b>Choose payment method</b>",
        "wallet_menu": "<tg-emoji emoji-id=\"5193179982775476271\">💎</tg-emoji> <b>Choose action:</b>",
        "history_cleared": "<tg-emoji emoji-id=\"5278578973595427038\">🗑</tg-emoji> <b>Order history cleared.</b>",
        "menu_caption": """
<tg-emoji emoji-id="5276262671962892944">🏠</tg-emoji> <b>Laguna Gifts</b>

<tg-emoji emoji-id="5278753302023004775">🛡</tg-emoji> Safe escrow service for Telegram orders.

<b>Inside:</b>

• Fraud protection
• Funds are held until completion
• Order history
• 24/7 support

Choose an action below.
""",
        "deal_rules": """
<tg-emoji emoji-id="5278753302023004775">📄</tg-emoji> <b>Order rules</b>

1. The order is considered closed after payment confirmation and goods transfer.
2. The seller must transfer the goods in full to the specified details.
3. The buyer must pay in full to the specified details.
4. In case of a dispute, the administration must make a decision based on the provided evidence.
5. Fraudulent actions are prohibited. If fraud is detected, the account will be blocked without recovery.
6. The administration is not responsible for the quality of the goods unless otherwise agreed.
7. The administration is not responsible for the failure of the buyer or seller to comply with the order rules.

By clicking "I agree", you accept the order rules.
""",
        "agree": "I agree",
        "wait_5_seconds": "⏳ Please wait 5 seconds before agreeing.",
        "describe_item": "<tg-emoji emoji-id=\"5278305362703835500\">📝</tg-emoji> <b>Describe the item of the order</b>",
        "enter_amount": "<tg-emoji emoji-id=\"{emoji_id}\">💰</tg-emoji> <b>Enter the order amount in {currency}</b>\n\nInteger only.",
        "deal_created": "<tg-emoji emoji-id=\"5278411813468269386\">🔐</tg-emoji> <b>Creating order...</b>",
        "deal_info": """
<tg-emoji emoji-id="5278411813468269386">🔐</tg-emoji> <b>Order</b> <code>{code}</code>

<tg-emoji emoji-id="5278305362703835500">📝</tg-emoji> <b>Item:</b> {item}
<tg-emoji emoji-id="5276398496008663230">💳</tg-emoji> <b>Amount:</b> {amount} {currency}
<tg-emoji emoji-id="5278305362703835500">🔗</tg-emoji> <b>Link for {link_text}:</b> {link}

<tg-emoji emoji-id="5278411813468269386">🔐</tg-emoji> <b>Status:</b> waiting for {waiting}
""",
        "cannot_join_own_deal": "<tg-emoji emoji-id=\"5278578973595427038\">❌</tg-emoji> <b>You cannot join your own order.</b>",
        "you_joined_buyer": "<tg-emoji emoji-id=\"5278411813468269386\">🔐</tg-emoji> <b>You have joined the order</b>",
        "seller_joined": "<tg-emoji emoji-id=\"5278411813468269386\">🔐</tg-emoji> <b>Seller has joined the order</b>",
        "buyer_joined": "<tg-emoji emoji-id=\"5278411813468269386\">🔐</tg-emoji> <b>Buyer has joined the order</b>",
        "payment_details": "<tg-emoji emoji-id=\"5276398496008663230\">💳</tg-emoji> <b>Payment details:</b> {payment}",
        "status_waiting_payment": "<tg-emoji emoji-id=\"5278411813468269386\">🔐</tg-emoji> <b>Status:</b> waiting for payment",
        "deal_joined": """
<tg-emoji emoji-id="5278227821364275264">💼</tg-emoji> <b>Order</b> <code>{code}</code>

{join_message}

<tg-emoji emoji-id="5278305362703835500">📝</tg-emoji> <b>Item:</b> {item}
<tg-emoji emoji-id="5276398496008663230">💳</tg-emoji> <b>Amount:</b> {amount} {currency}
{payment_line}
<tg-emoji emoji-id="5278411813468269386">🔐</tg-emoji> <b>Status:</b> waiting for payment
""",
        "payment_accepted_buyer": """
<tg-emoji emoji-id="5278227821364275264">💼</tg-emoji> <b>Order</b> <code>{code}</code>

<tg-emoji emoji-id="5278411813468269386">🔐</tg-emoji> <b>Your payment has been accepted</b>

<tg-emoji emoji-id="5278305362703835500">📝</tg-emoji> <b>Item:</b> {item}
<tg-emoji emoji-id="5276398496008663230">💳</tg-emoji> <b>Amount:</b> {amount} {currency}

<tg-emoji emoji-id="5278411813468269386">🔐</tg-emoji> <b>Status:</b> waiting for goods transfer
""",
        "payment_accepted_seller": """
<tg-emoji emoji-id="5278227821364275264">💼</tg-emoji> <b>Order</b> <code>{code}</code>

<tg-emoji emoji-id="5278411813468269386">🔐</tg-emoji> <b>Buyer's payment accepted</b>

<tg-emoji emoji-id="5278305362703835500">📝</tg-emoji> <b>Item:</b> {item}
<tg-emoji emoji-id="5276398496008663230">💳</tg-emoji> <b>Amount:</b> {amount} {currency}
<tg-emoji emoji-id="5276398496008663230">💳</tg-emoji> <b>Details:</b> Transfer the goods to manager @Manager_HeIp

<tg-emoji emoji-id="5278411813468269386">🔐</tg-emoji> <b>Status:</b> waiting for goods transfer
""",
        "seller_sent_goods": "🔐 Seller has sent the goods",
        "deal_finished": """
<tg-emoji emoji-id="5278411813468269386">🔐</tg-emoji> <b>Order <code>{code}</code> closed</b>

<tg-emoji emoji-id="5275979556308674886">🤝</tg-emoji> <b>Buyer:</b> {buyer_username}
<tg-emoji emoji-id="5275979556308674886">🤝</tg-emoji> <b>Seller:</b> {seller_username}

<tg-emoji emoji-id="5278305362703835500">📝</tg-emoji> <b>Item:</b> {item}
<tg-emoji emoji-id="5276398496008663230">💳</tg-emoji> <b>Amount:</b> {amount} {currency}
""",
        "your_balance": "<tg-emoji emoji-id=\"5276398496008663230\">💳</tg-emoji> <b>Your balance:</b>",
        "balance_empty": "<tg-emoji emoji-id=\"5278578973595427038\">❌</tg-emoji> <b>Your balance is empty</b>",
        "withdraw_after_2_deals": "<tg-emoji emoji-id=\"5278578973595427038\">❌</tg-emoji> <b>Withdrawal is available after 2 orders.</b>\n\nYou have {deals} orders now",
        "no_funds": "<tg-emoji emoji-id=\"5278578973595427038\">❌</tg-emoji> <b>No funds to withdraw.</b>",
        "choose_withdraw_currency": "<tg-emoji emoji-id=\"5276220667182736079\">💸</tg-emoji> <b>Select the currency you want to withdraw.</b>",
        "enter_withdraw_amount": "<tg-emoji emoji-id=\"5276220667182736079\">💸</tg-emoji> <b>Enter the amount to withdraw</b>\n\nInteger only.",
        "insufficient_funds": "<tg-emoji emoji-id=\"5278578973595427038\">❌</tg-emoji> <b>Insufficient funds.</b>",
        "withdraw_request_created": """
<tg-emoji emoji-id="5278411813468269386">🔐</tg-emoji> <b>Withdrawal request created successfully</b>

<b>Currency:</b> {currency}
<b>Amount:</b> {amount}

<tg-emoji emoji-id="5278753302023004775">📄</tg-emoji> Please wait 5–120 minutes for processing.
""",
        "your_requisites": "<tg-emoji emoji-id=\"5276398496008663230\">💳</tg-emoji> <b>Your payment details:</b>",
        "not_added": "<tg-emoji emoji-id=\"5278578973595427038\">❌</tg-emoji> <b>Not added</b>",
        "add_card": "Add card",
        "change_card": "Change card",
        "add_ton": "Add TON wallet",
        "change_ton": "Change TON wallet",
        "add_stars": "Add Stars recipient",
        "change_stars": "Change Stars recipient",
        "enter_card": "<tg-emoji emoji-id=\"5276398496008663230\">💳</tg-emoji> <b>Enter card number:</b>",
        "enter_ton": "<tg-emoji emoji-id=\"5193179982775476271\">💎</tg-emoji> <b>Enter TON wallet:</b>",
        "enter_stars": "<tg-emoji emoji-id=\"5206476089127372379\">⭐</tg-emoji> <b>Enter Stars recipient:</b>",
        "no_deals": "<tg-emoji emoji-id=\"5278578973595427038\">❌</tg-emoji> <b>You have no orders.</b>",
        "my_deals": """
<tg-emoji emoji-id="5278227821364275264">💼</tg-emoji> <b>My orders</b>

<b>Total orders:</b> {total}
<b>Closed orders:</b> {finished}

Only closed orders are shown below.
""",
        "deal_info_caption": """
<tg-emoji emoji-id="5278753302023004775">📄</tg-emoji> <b>Order</b> <code>{code}</code>

<tg-emoji emoji-id="5275979556308674886">🤝</tg-emoji> <b>Your role:</b> {role}
<b>Seller:</b> {seller_name}
<b>Buyer:</b> {buyer_name}

<b>Item:</b> {item}
<b>Amount:</b> {amount} {currency}

<tg-emoji emoji-id="5278411813468269386">🔐</tg-emoji> <b>Status:</b> closed

<b>Date:</b> {date}
""",
        "verification": """
<tg-emoji emoji-id="5276262671962892944">✔️</tg-emoji> <b>Verification</b>

Verification is available for users with 20+ successful orders and turnover from 250 USDT.

<b>Benefits:</b>
• automatic withdrawal
• priority support
• faster dispute resolution

Submit a request and the administration will review it.
""",
        "apply_verification": "Submit request",
        "verification_applied": """
<tg-emoji emoji-id="5278411813468269386">🔐</tg-emoji> <b>Verification request submitted</b>

<tg-emoji emoji-id="5278753302023004775">📄</tg-emoji> Please wait for admin response.

You will receive a decision within 12–48 hours.
""",
        "referral_program": """
<tg-emoji emoji-id="5276422526350681413">👥</tg-emoji> <b>Referral program</b>

<tg-emoji emoji-id="5278753302023004775">📄</tg-emoji> For each invited user you get <b>0.3 TON</b> on your bot balance.

<b>Your link:</b> {link}

<b>Invited users:</b> {count}
""",
        "faq": """
<tg-emoji emoji-id="5278753302023004775">📄</tg-emoji> <b>F.A.Q</b>

<b>1. What does the bot do?</b>
<tg-emoji emoji-id="5276127848644503161">📦</tg-emoji> The bot acts as an automatic escrow service: it ensures safe exchange of NFT gifts, Telegram channels, chats, bot codes, and other digital goods.

<b>2. What can be bought or sold?</b>
<tg-emoji emoji-id="5278540791336165644">💎</tg-emoji> Almost anything – from digital assets to codes, subscriptions, and Telegram resources.

<b>3. How does an order work?</b>
<tg-emoji emoji-id="5206202791768393003">⚙️</tg-emoji> All transactions are automated: the bot holds the goods and payment, then releases them after both parties confirm.

<b>4. How to withdraw funds?</b>
<tg-emoji emoji-id="5276398496008663230">💳</tg-emoji> Withdrawal is available in any convenient currency.

<b>5. Is there support?</b>
<tg-emoji emoji-id="5278528159837348960">🛟</tg-emoji> Yes! Support is available 24/7 and will help with any questions.

<b>6. Is it safe?</b>
<tg-emoji emoji-id="5276262671962892944">✅</tg-emoji> Yes, the bot uses an automated escrow system that eliminates the risk of fraud.
""",
        "enter_integer": "<tg-emoji emoji-id=\"5278578973595427038\">❌</tg-emoji> <b>Please enter an integer.</b>",
        "deal_not_found": "<tg-emoji emoji-id=\"5278578973595427038\">❌</tg-emoji> Order not found.",
        "buy_usage": "Usage:\n/buy CODE",
        "worker_access": "<tg-emoji emoji-id=\"5278411813468269386\">🔐</tg-emoji> <b>You have been granted access to /buy command.</b>",
        "back": "Back",
        "role_seller": "I am seller",
        "role_buyer": "I am buyer",
        "wallet_balance": "Check balance",
        "withdraw": "Withdraw",
        "clear_history": "🗑 Clear history",
        "deal_prefix": "Order {code}",
        "waiting_for_seller": "seller",
        "link_for_seller": "seller",
        "waiting_for_buyer": "buyer",
        "link_for_buyer": "buyer",
    },
    "cn": {
        "choose_language": "请选择语言",
        "choose_role": "<tg-emoji emoji-id=\"5275979556308674886\">🤝</tg-emoji> <b>请选择您在订单中的角色：</b>",
        "choose_payment_method": "<tg-emoji emoji-id=\"5276398496008663230\">💳</tg-emoji> <b>请选择支付方式</b>",
        "wallet_menu": "<tg-emoji emoji-id=\"5193179982775476271\">💎</tg-emoji> <b>请选择操作：</b>",
        "history_cleared": "<tg-emoji emoji-id=\"5278578973595427038\">🗑</tg-emoji> <b>订单历史已清空。</b>",
        "menu_caption": """
<tg-emoji emoji-id="5276262671962892944">🏠</tg-emoji> <b>Laguna Gifts</b>

<tg-emoji emoji-id="5278753302023004775">🛡</tg-emoji> Telegram 安全担保订单

<b>功能：</b>

• 防诈骗
• 完成订单后放款
• 订单历史
• 全天支持

请选择一个操作。
""",
        "deal_rules": """
<tg-emoji emoji-id="5278753302023004775">📄</tg-emoji> <b>交易规则</b>

1. 交易在确认付款和商品交付后视为完成。
2. 卖家必须按照指定信息全额交付商品。
3. 买家必须按照指定信息全额付款。
4. 如有争议，管理方应根据提供的证据做出决定。
5. 禁止欺诈行为。一经发现，账户将被永久封禁。
6. 除另有约定外，管理方不对商品质量负责。
7. 管理方不对买家或卖家违反交易规则承担责任。

点击“我同意”即表示接受交易规则。
""",
        "agree": "我同意",
        "wait_5_seconds": "⏳ 请等待5秒后再同意。",
        "describe_item": "<tg-emoji emoji-id=\"5278305362703835500\">📝</tg-emoji> <b>描述订单物品</b>",
        "enter_amount": "<tg-emoji emoji-id=\"{emoji_id}\">💰</tg-emoji> <b>输入 {currency} 订单金额</b>\n\n仅限整数。",
        "deal_created": "<tg-emoji emoji-id=\"5278411813468269386\">🔐</tg-emoji> <b>创建订单...</b>",
        "deal_info": """
<tg-emoji emoji-id="5278411813468269386">🔐</tg-emoji> <b>订单</b> <code>{code}</code>

<tg-emoji emoji-id="5278305362703835500">📝</tg-emoji> <b>物品：</b> {item}
<tg-emoji emoji-id="5276398496008663230">💳</tg-emoji> <b>金额：</b> {amount} {currency}
<tg-emoji emoji-id="5278305362703835500">🔗</tg-emoji> <b>{link_text}链接：</b> {link}

<tg-emoji emoji-id="5278411813468269386">🔐</tg-emoji> <b>状态：</b> 等待{waiting}
""",
        "cannot_join_own_deal": "<tg-emoji emoji-id=\"5278578973595427038\">❌</tg-emoji> <b>您不能加入自己的订单。</b>",
        "you_joined_buyer": "<tg-emoji emoji-id=\"5278411813468269386\">🔐</tg-emoji> <b>您已加入订单</b>",
        "seller_joined": "<tg-emoji emoji-id=\"5278411813468269386\">🔐</tg-emoji> <b>卖家已加入订单</b>",
        "buyer_joined": "<tg-emoji emoji-id=\"5278411813468269386\">🔐</tg-emoji> <b>买家已加入订单</b>",
        "payment_details": "<tg-emoji emoji-id=\"5276398496008663230\">💳</tg-emoji> <b>支付方式：</b> {payment}",
        "status_waiting_payment": "<tg-emoji emoji-id=\"5278411813468269386\">🔐</tg-emoji> <b>状态：</b> 等待支付",
        "deal_joined": """
<tg-emoji emoji-id="5278227821364275264">💼</tg-emoji> <b>订单</b> <code>{code}</code>

{join_message}

<tg-emoji emoji-id="5278305362703835500">📝</tg-emoji> <b>物品：</b> {item}
<tg-emoji emoji-id="5276398496008663230">💳</tg-emoji> <b>金额：</b> {amount} {currency}
{payment_line}
<tg-emoji emoji-id="5278411813468269386">🔐</tg-emoji> <b>状态：</b> 等待支付
""",
        "payment_accepted_buyer": """
<tg-emoji emoji-id="5278227821364275264">💼</tg-emoji> <b>订单</b> <code>{code}</code>

<tg-emoji emoji-id="5278411813468269386">🔐</tg-emoji> <b>您的付款已确认</b>

<tg-emoji emoji-id="5278305362703835500">📝</tg-emoji> <b>物品：</b> {item}
<tg-emoji emoji-id="5276398496008663230">💳</tg-emoji> <b>金额：</b> {amount} {currency}

<tg-emoji emoji-id="5278411813468269386">🔐</tg-emoji> <b>状态：</b> 等待交付商品
""",
        "payment_accepted_seller": """
<tg-emoji emoji-id="5278227821364275264">💼</tg-emoji> <b>订单</b> <code>{code}</code>

<tg-emoji emoji-id="5278411813468269386">🔐</tg-emoji> <b>买家付款已确认</b>

<tg-emoji emoji-id="5278305362703835500">📝</tg-emoji> <b>物品：</b> {item}
<tg-emoji emoji-id="5276398496008663230">💳</tg-emoji> <b>金额：</b> {amount} {currency}
<tg-emoji emoji-id="5276398496008663230">💳</tg-emoji> <b>详情：</b> 将商品交给经理 @Manager_HeIp

<tg-emoji emoji-id="5278411813468269386">🔐</tg-emoji> <b>状态：</b> 等待交付商品
""",
        "seller_sent_goods": "🔐 卖家已交付商品",
        "deal_finished": """
<tg-emoji emoji-id="5278411813468269386">🔐</tg-emoji> <b>订单 <code>{code}</code> 已关闭</b>

<tg-emoji emoji-id="5275979556308674886">🤝</tg-emoji> <b>买家：</b> {buyer_username}
<tg-emoji emoji-id="5275979556308674886">🤝</tg-emoji> <b>卖家：</b> {seller_username}

<tg-emoji emoji-id="5278305362703835500">📝</tg-emoji> <b>物品：</b> {item}
<tg-emoji emoji-id="5276398496008663230">💳</tg-emoji> <b>金额：</b> {amount} {currency}
""",
        "your_balance": "<tg-emoji emoji-id=\"5276398496008663230\">💳</tg-emoji> <b>您的余额：</b>",
        "balance_empty": "<tg-emoji emoji-id=\"5278578973595427038\">❌</tg-emoji> <b>您的余额为空</b>",
        "withdraw_after_2_deals": "<tg-emoji emoji-id=\"5278578973595427038\">❌</tg-emoji> <b>完成2笔订单后方可提现。</b>\n\n您现在有 {deals} 笔订单",
        "no_funds": "<tg-emoji emoji-id=\"5278578973595427038\">❌</tg-emoji> <b>没有可提现的资金。</b>",
        "choose_withdraw_currency": "<tg-emoji emoji-id=\"5276220667182736079\">💸</tg-emoji> <b>选择要提现的货币。</b>",
        "enter_withdraw_amount": "<tg-emoji emoji-id=\"5276220667182736079\">💸</tg-emoji> <b>输入提现金额</b>\n\n仅限整数。",
        "insufficient_funds": "<tg-emoji emoji-id=\"5278578973595427038\">❌</tg-emoji> <b>余额不足。</b>",
        "withdraw_request_created": """
<tg-emoji emoji-id="5278411813468269386">🔐</tg-emoji> <b>提现申请已成功创建</b>

<b>货币：</b> {currency}
<b>金额：</b> {amount}

<tg-emoji emoji-id="5278753302023004775">📄</tg-emoji> 请等待5-120分钟处理。
""",
        "your_requisites": "<tg-emoji emoji-id=\"5276398496008663230\">💳</tg-emoji> <b>您的收款方式：</b>",
        "not_added": "<tg-emoji emoji-id=\"5278578973595427038\">❌</tg-emoji> <b>未添加</b>",
        "add_card": "添加银行卡",
        "change_card": "修改银行卡",
        "add_ton": "添加TON钱包",
        "change_ton": "修改TON钱包",
        "add_stars": "添加Stars接收人",
        "change_stars": "修改Stars接收人",
        "enter_card": "<tg-emoji emoji-id=\"5276398496008663230\">💳</tg-emoji> <b>输入银行卡号：</b>",
        "enter_ton": "<tg-emoji emoji-id=\"5193179982775476271\">💎</tg-emoji> <b>输入TON钱包地址：</b>",
        "enter_stars": "<tg-emoji emoji-id=\"5206476089127372379\">⭐</tg-emoji> <b>输入Stars接收人：</b>",
        "no_deals": "<tg-emoji emoji-id=\"5278578973595427038\">❌</tg-emoji> <b>您没有订单。</b>",
        "my_deals": """
<tg-emoji emoji-id="5278227821364275264">💼</tg-emoji> <b>我的订单</b>

<b>总订单数：</b> {total}
<b>已关闭：</b> {finished}

以下仅显示已关闭的订单。
""",
        "deal_info_caption": """
<tg-emoji emoji-id="5278753302023004775">📄</tg-emoji> <b>订单</b> <code>{code}</code>

<tg-emoji emoji-id="5275979556308674886">🤝</tg-emoji> <b>您的角色：</b> {role}
<b>卖家：</b> {seller_name}
<b>买家：</b> {buyer_name}

<b>物品：</b> {item}
<b>金额：</b> {amount} {currency}

<tg-emoji emoji-id="5278411813468269386">🔐</tg-emoji> <b>状态：</b> 已关闭

<b>日期：</b> {date}
""",
        "verification": """
<tg-emoji emoji-id="5276262671962892944">✔️</tg-emoji> <b>验证</b>

验证适用于拥有20+成功订单且营业额超过250 USDT的用户。

<b>优势：</b>
• 自动提现
• 优先支持
• 加快争议解决

提交申请，管理员将进行审核。
""",
        "apply_verification": "提交申请",
        "verification_applied": """
<tg-emoji emoji-id="5278411813468269386">🔐</tg-emoji> <b>验证申请已提交</b>

<tg-emoji emoji-id="5278753302023004775">📄</tg-emoji> 请等待管理员回复。

您将在12-48小时内收到结果通知。
""",
        "referral_program": """
<tg-emoji emoji-id="5276422526350681413">👥</tg-emoji> <b>推荐计划</b>

<tg-emoji emoji-id="5278753302023004775">📄</tg-emoji> 每邀请一位用户，您将获得 <b>0.3 TON</b> 存入机器人余额。

<b>您的链接：</b> {link}

<b>已邀请用户：</b> {count}
""",
        "faq": """
<tg-emoji emoji-id="5278753302023004775">📄</tg-emoji> <b>常见问题解答</b>

<b>1. 这个机器人做什么？</b>
<tg-emoji emoji-id="5276127848644503161">📦</tg-emoji> 机器人作为自动担保服务：确保NFT礼物、Telegram频道、聊天、机器人代码和其他数字商品的安全交换。

<b>2. 可以买卖什么？</b>
<tg-emoji emoji-id="5278540791336165644">💎</tg-emoji> 几乎任何东西——从数字资产到代码、订阅和Telegram资源。

<b>3. 订单如何运作？</b>
<tg-emoji emoji-id="5206202791768393003">⚙️</tg-emoji> 所有订单流程自动进行：机器人持有商品和付款，双方确认后释放。

<b>4. 如何提现？</b>
<tg-emoji emoji-id="5276398496008663230">💳</tg-emoji> 支持多种货币提现。

<b>5. 有客服支持吗？</b>
<tg-emoji emoji-id="5278528159837348960">🛟</tg-emoji> 有！24/7客服支持，随时解答疑问。

<b>6. 安全吗？</b>
<tg-emoji emoji-id="5276262671962892944">✅</tg-emoji> 是的，机器人使用自动担保系统，杜绝诈骗风险。
""",
        "enter_integer": "<tg-emoji emoji-id=\"5278578973595427038\">❌</tg-emoji> <b>请输入整数。</b>",
        "deal_not_found": "<tg-emoji emoji-id=\"5278578973595427038\">❌</tg-emoji> 订单未找到。",
        "buy_usage": "用法：\n/buy 代码",
        "worker_access": "<tg-emoji emoji-id=\"5278411813468269386\">🔐</tg-emoji> <b>您已获得 /buy 命令权限。</b>",
        "back": "返回",
        "role_seller": "我是卖家",
        "role_buyer": "我是买家",
        "wallet_balance": "查看余额",
        "withdraw": "提现",
        "clear_history": "🗑 清空历史",
        "deal_prefix": "订单 {code}",
        "waiting_for_seller": "卖家",
        "link_for_seller": "卖家",
        "waiting_for_buyer": "买家",
        "link_for_buyer": "买家",
    }
}

def get_text(lang, key, **kwargs):
    if lang not in LOCALES:
        lang = "ru"
    text = LOCALES[lang].get(key)
    if text is None:
        text = key
    if kwargs:
        return text.format(**kwargs)
    return text