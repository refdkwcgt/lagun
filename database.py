import sqlite3

from datetime import datetime

db = sqlite3.connect("users.db", check_same_thread=False)
cursor = db.cursor()


# ---------------- USERS ----------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER PRIMARY KEY,
    language TEXT NOT NULL,
    worker INTEGER DEFAULT 0
)
""")


# если колонка worker отсутствует
try:
    cursor.execute("ALTER TABLE users ADD COLUMN worker INTEGER DEFAULT 0")
except:
    pass
    
try:
    cursor.execute("ALTER TABLE users ADD COLUMN username TEXT")
except:
    pass
    
   
cursor.execute("""
CREATE TABLE IF NOT EXISTS referrals(
    user_id INTEGER PRIMARY KEY,
    inviter_id INTEGER
)
""")

db.commit()

    
# ---------------- REQUISITES ----------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS requisites(
    user_id INTEGER PRIMARY KEY,
    card TEXT,
    ton TEXT,
    stars TEXT
)
""")

db.commit()


# ---------------- DEALS ----------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS deals(
    code TEXT PRIMARY KEY,
    creator_id INTEGER,
    creator_role TEXT,
    item TEXT,
    amount TEXT,
    currency TEXT,
    partner_id INTEGER,
    status TEXT,
    buyer_id INTEGER,
    seller_id INTEGER,
    buyer_message INTEGER,
    seller_message INTEGER
)
""")

db.commit()

try:
    cursor.execute("ALTER TABLE deals ADD COLUMN date TEXT")
except:
    pass

db.commit()

cursor.execute("""
CREATE TABLE IF NOT EXISTS wallets(
    user_id INTEGER PRIMARY KEY,
    rub INTEGER DEFAULT 0,
    uah INTEGER DEFAULT 0,
    byn INTEGER DEFAULT 0,
    ton REAL DEFAULT 0,
    stars INTEGER DEFAULT 0,
    deals INTEGER DEFAULT 0
)
""")

def set_finish_date(code):

    cursor.execute(
        """
        UPDATE deals
        SET date=?
        WHERE code=?
        """,
        (
            datetime.now().strftime("%d.%m.%Y %H:%M"),
            code
        )
    )

    db.commit()
    
cursor.execute("""
CREATE TABLE IF NOT EXISTS blacklist(
    user_id INTEGER PRIMARY KEY,
    reason TEXT
)
""")

db.commit()
    
# =======================
# ЯЗЫК
# =======================

def get_language(user_id):

    cursor.execute(
        "SELECT language FROM users WHERE user_id=?",
        (user_id,)
    )

    row = cursor.fetchone()

    if row:
        return row[0]

    return None


def set_language(user_id, lang):

    cursor.execute("""
    INSERT INTO users(user_id, language)
    VALUES(?,?)

    ON CONFLICT(user_id)

    DO UPDATE SET language=excluded.language
    """, (user_id, lang))

    db.commit()


# =======================
# WORKER
# =======================

def add_worker(user_id):

    cursor.execute("""
    INSERT INTO users(user_id, language, worker)
    VALUES(?, 'ru', 1)

    ON CONFLICT(user_id)
    DO UPDATE SET worker=1
    """, (user_id,))

    db.commit()


def is_worker(user_id):

    cursor.execute(
        "SELECT worker FROM users WHERE user_id=?",
        (user_id,)
    )

    row = cursor.fetchone()

    if not row:
        return False

    return row[0] == 1


# =======================
# DEALS
# =======================

def create_deal(
    code,
    creator_id,
    role,
    item,
    amount,
    currency
):

    cursor.execute("""
    INSERT INTO deals(
        code,
        creator_id,
        creator_role,
        item,
        amount,
        currency,
        status
    )
    VALUES(?,?,?,?,?,?,?)
    """,
    (
        code,
        creator_id,
        role,
        item,
        amount,
        currency,
        "waiting"
    ))

    db.commit()


def get_deal(code):

    cursor.execute(
        "SELECT * FROM deals WHERE code=?",
        (code,)
    )

    return cursor.fetchone()
    
def get_user_finished_deals(user_id):

    cursor.execute("""
    SELECT *
    FROM deals
    WHERE status='finished'
    AND (buyer_id=? OR seller_id=?)
    ORDER BY rowid DESC
    """,
    (
        user_id,
        user_id
    ))

    return cursor.fetchall()


def connect_deal(code, buyer_id, seller_id):

    cursor.execute("""
    UPDATE deals
    SET
        partner_id=?,
        buyer_id=?,
        seller_id=?
    WHERE code=?
    """,
    (
        buyer_id,
        buyer_id,
        seller_id,
        code
    ))

    db.commit()


def update_status(code, status):

    cursor.execute(
        "UPDATE deals SET status=? WHERE code=?",
        (status, code)
    )

    db.commit()


def save_messages(
    code,
    buyer_message,
    seller_message
):

    cursor.execute("""
    UPDATE deals
    SET
        buyer_message=?,
        seller_message=?
    WHERE code=?
    """,
    (
        buyer_message,
        seller_message,
        code
    ))

    db.commit()


def get_buyer(code):

    cursor.execute(
        "SELECT buyer_id FROM deals WHERE code=?",
        (code,)
    )

    row = cursor.fetchone()

    return row[0]


def get_seller(code):

    cursor.execute(
        "SELECT seller_id FROM deals WHERE code=?",
        (code,)
    )

    row = cursor.fetchone()

    return row[0]


def get_messages(code):

    cursor.execute("""
    SELECT buyer_message, seller_message
    FROM deals
    WHERE code=?
    """,
    (code,)
    )

    return cursor.fetchone()
    
def get_finished_deals_count(user_id):

    cursor.execute("""
    SELECT COUNT(*)
    FROM deals
    WHERE status='finished'
    AND (buyer_id=? OR seller_id=?)
    """,
    (
        user_id,
        user_id
    ))

    return cursor.fetchone()[0]

    
def get_requisites(user_id):

    cursor.execute(
        "SELECT card, ton, stars FROM requisites WHERE user_id=?",
        (user_id,)
    )

    row = cursor.fetchone()

    if not row:
        return {
            "card": None,
            "ton": None,
            "stars": None
        }

    return {
        "card": row[0],
        "ton": row[1],
        "stars": row[2]
    }


def set_requisite(user_id, field, value):

    cursor.execute("""
    INSERT INTO requisites(user_id)
    VALUES(?)
    ON CONFLICT(user_id)
    DO NOTHING
    """,
    (user_id,))

    cursor.execute(
        f"""
        UPDATE requisites
        SET {field}=?
        WHERE user_id=?
        """,
        (
            value,
            user_id
        )
    )

    db.commit()
    
def get_wallet(user_id):
    cursor.execute(
        "SELECT rub, uah, byn, ton, stars, deals FROM wallets WHERE user_id=?",
        (user_id,)
    )

    row = cursor.fetchone()

    if row:
        return row

    cursor.execute(
        "INSERT INTO wallets(user_id) VALUES(?)",
        (user_id,)
    )

    db.commit()

    return (0,0,0,0,0,0)
  
def add_balance(user_id, currency, amount):

    get_wallet(user_id)

    field = currency.lower()

    cursor.execute(
        f"UPDATE wallets SET {field}={field}+? WHERE user_id=?",
        (amount,user_id)
    )

    db.commit()
    
def add_deal_count(user_id):

    get_wallet(user_id)

    cursor.execute(
        "UPDATE wallets SET deals=deals+1 WHERE user_id=?",
        (user_id,)
    )

    db.commit()
    
def get_deal_count(user_id):

    get_wallet(user_id)

    cursor.execute(
        "SELECT deals FROM wallets WHERE user_id=?",
        (user_id,)
    )

    row = cursor.fetchone()

    return row[0]
    
    
def get_total_balance(user_id):

    rub, uah, byn, ton, stars, deals = get_wallet(user_id)

    return (
        rub > 0 or
        uah > 0 or
        byn > 0 or
        ton > 0 or
        stars > 0
    )
    
def remove_balance(user_id, currency, amount):

    get_wallet(user_id)

    field = currency.lower()

    cursor.execute(
        f"""
        UPDATE wallets
        SET {field}={field}-?
        WHERE user_id=?
        """,
        (
            amount,
            user_id
        )
    )

    db.commit()
    
def get_finished_deal(code):

    cursor.execute(
        """
        SELECT *
        FROM deals
        WHERE code=?
        AND status='finished'
        """,
        (code,)
    )

    return cursor.fetchone()
    
def get_user_role(code, user_id):

    deal = get_deal(code)

    if not deal:
        return None

    if deal[8] == user_id:
        return "Покупатель"

    if deal[9] == user_id:
        return "Продавец"

    return None
    
def has_balance(user_id, currency, amount):

    wallet = get_wallet(user_id)

    fields = {
        "RUB":0,
        "UAH":1,
        "BYN":2,
        "TON":3,
        "STARS":4
    }

    return wallet[fields[currency]] >= amount
    
def get_currency_balance(user_id, currency):

    wallet = get_wallet(user_id)

    fields = {
        "RUB":0,
        "UAH":1,
        "BYN":2,
        "TON":3,
        "STARS":4
    }

    return wallet[fields[currency]]
    
def get_finished_codes(user_id):

    cursor.execute("""
    SELECT code
    FROM deals
    WHERE status='finished'
    AND (buyer_id=? OR seller_id=?)
    ORDER BY rowid DESC
    """,
    (
        user_id,
        user_id
    ))

    return [i[0] for i in cursor.fetchall()]
    
def add_referral(user_id, inviter_id):

    # нельзя пригласить самого себя
    if user_id == inviter_id:
        return False


    # проверяем, был ли уже приглашен
    cursor.execute(
        """
        SELECT inviter_id
        FROM referrals
        WHERE user_id=?
        """,
        (user_id,)
    )

    if cursor.fetchone():
        return False


    # записываем реферала
    cursor.execute(
        """
        INSERT INTO referrals(user_id, inviter_id)
        VALUES(?,?)
        """,
        (user_id, inviter_id)
    )


    db.commit()


    # начисляем 0.3 TON на основной баланс
    add_balance(
        inviter_id,
        "TON",
        0.3
    )


    return True


def get_referrals_count(inviter_id):

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM referrals
        WHERE inviter_id=?
        """,
        (inviter_id,)
    )

    return cursor.fetchone()[0]
    

def save_username(user_id, username):
    """Обновляет username у существующего пользователя. Если пользователя нет — ничего не делает."""
    cursor.execute(
        "UPDATE users SET username = ? WHERE user_id = ?",
        (username, user_id)
    )
    db.commit()


def get_user_by_username(username):

    cursor.execute(
        """
        SELECT user_id
        FROM users
        WHERE username=?
        """,
        (username,)
    )

    row = cursor.fetchone()

    if row:
        return row[0]

    return None



def add_blacklist(user_id, reason=""):

    cursor.execute("""
    INSERT OR IGNORE INTO blacklist(user_id, reason)
    VALUES(?,?)
    """,
    (
        user_id,
        reason
    ))

    db.commit()



def remove_blacklist(user_id):

    cursor.execute(
        "DELETE FROM blacklist WHERE user_id=?",
        (user_id,)
    )

    db.commit()



def is_blacklisted(user_id):

    cursor.execute(
        "SELECT user_id FROM blacklist WHERE user_id=?",
        (user_id,)
    )

    return cursor.fetchone() is not None
    
def get_all_users():

    cursor.execute(
        "SELECT user_id FROM users"
    )

    return cursor.fetchall()



def get_all_workers():

    cursor.execute(
        """
        SELECT user_id
        FROM users
        WHERE worker=1
        """
    )

    return cursor.fetchall()
    
def get_users_count():

    cursor.execute(
        "SELECT COUNT(*) FROM users"
    )

    return cursor.fetchone()[0]


def get_workers_count():

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM users
        WHERE worker=1
        """
    )

    return cursor.fetchone()[0]


def get_today_finished_deals():

    today = datetime.now().strftime("%d.%m.%Y")

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM deals
        WHERE status='finished'
        AND date LIKE ?
        """,
        (today+"%",)
    )

    return cursor.fetchone()[0]


def get_new_users_today():

    today = datetime.now().strftime("%d.%m.%Y")

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM users
        WHERE date LIKE ?
        """,
        (today+"%",)
    )

    return cursor.fetchone()[0]
    
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def admin_keyboard():

    return InlineKeyboardMarkup(
        inline_keyboard=[

            [
                InlineKeyboardButton(
                    text="📢 Рассылка",
                    callback_data="admin_send"
                )
            ],

            [
                InlineKeyboardButton(
                    text="👤 Пользователь",
                    callback_data="admin_user"
                )
            ],

            [
                InlineKeyboardButton(
                    text="📊 Статистика",
                    callback_data="admin_stats"
                )
            ],

            [
                InlineKeyboardButton(
                    text="🤝 Воркеры",
                    callback_data="admin_workers"
                )
            ],

            [
                InlineKeyboardButton(
                    text="🚫 Черный список",
                    callback_data="admin_blacklist"
                )
            ]

        ]
    )
    
def get_users_count():

    cursor.execute(
        "SELECT COUNT(*) FROM users"
    )

    return cursor.fetchone()[0]


def get_workers_count():

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM users
        WHERE worker=1
        """
    )

    return cursor.fetchone()[0]


def get_today_finished_deals():

    today = datetime.now().strftime("%d.%m.%Y")

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM deals
        WHERE status='finished'
        AND date LIKE ?
        """,
        (
            today + "%",
        )
    )

    return cursor.fetchone()[0]


def get_new_users_today():

    # если даты пользователей ещё нет
    # временно возвращаем количество новых за сегодня
    return 0


def get_workers():

    cursor.execute(
        """
        SELECT user_id
        FROM users
        WHERE worker=1
        """
    )

    return cursor.fetchall()


def remove_worker(user_id):

    cursor.execute(
        """
        UPDATE users
        SET worker=0
        WHERE user_id=?
        """,
        (
            user_id,
        )
    )

    db.commit()
    
def get_user_by_username(username):

    cursor.execute(
        """
        SELECT user_id
        FROM users
        WHERE username=?
        """,
        (username,)
    )

    row = cursor.fetchone()

    if row:
        return row[0]

    return None
    
cursor.execute("""
CREATE TABLE IF NOT EXISTS blacklist(
    user_id INTEGER PRIMARY KEY
)
""")

db.commit()


def add_blacklist(user_id):

    cursor.execute(
        """
        INSERT OR IGNORE INTO blacklist(user_id)
        VALUES(?)
        """,
        (user_id,)
    )

    db.commit()



def remove_blacklist(user_id):

    cursor.execute(
        """
        DELETE FROM blacklist
        WHERE user_id=?
        """,
        (user_id,)
    )

    db.commit()



def is_blacklisted(user_id):

    cursor.execute(
        """
        SELECT user_id
        FROM blacklist
        WHERE user_id=?
        """,
        (user_id,)
    )

    return cursor.fetchone() is not None



def get_blacklist_count():

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM blacklist
        """
    )

    return cursor.fetchone()[0]
