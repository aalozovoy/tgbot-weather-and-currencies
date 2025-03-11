import os
import sqlite3



# Получить абсолютный путь к директории, в которой находится main.py
base_dir = os.path.dirname(__file__)

# Путь к базе данных SQLite
db_path = os.path.join(base_dir, 'bot_history.db')

# Функция для инициализации базы данных
def init_db():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS history (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER,
                        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                        name TEXT,                    
                        mess TEXT                      
                      )''')
    conn.commit()
    conn.close()


# Функция для записи истории запросов
def log_history(user_id, full_name, mess):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO history (user_id, name, mess) VALUES (?, ?, ?)', (user_id, full_name, mess))
    conn.commit()
    conn.close()



# Функция для чтения истории запросов
def get_history(user_id):
    max_length = 4070
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT mess, timestamp, name FROM history WHERE user_id = ? ORDER BY timestamp ASC', (user_id,))
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        return "История запросов пуста."

    history = "\n".join([f"{timestamp}|{name}: {mess}" for mess, timestamp, name in rows])
    return history[-max_length:]











