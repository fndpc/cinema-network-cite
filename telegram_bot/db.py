import sqlalchemy
from pathlib import Path

def check_id_in_db(token: str, chat_id: str) -> tuple[bool, str]:
    db_path = Path('/home/user/dev/cinema-network-cite/website/db.sqlite3')
    engine = sqlalchemy.create_engine(f"sqlite:///{db_path}", echo=True)
    
    with engine.connect() as conn:
        result = conn.execute(sqlalchemy.text("SELECT email, token, telegram_chat_id FROM users_customuser"))
        for row in result:
            email, db_token, chat_id_from_db = row
            if db_token == token:
                if chat_id_from_db and chat_id_from_db != '':
                    return (True, email)
                else:
                    conn.execute(
                        sqlalchemy.text("UPDATE users_customuser SET telegram_chat_id = :chat_id WHERE token = :token"),
                        {"chat_id": chat_id, "token": token}
                    )
                    conn.commit()
                    return (False, email)