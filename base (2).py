import sqlite3

class SQL:
    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()
    #добавление пользователя в бд
    def add_user(self, id):
        with self.connection:
            return self.cursor.execute("INSERT INTO users (id) VALUES(?)", (id,))
    #проверка, есть ли пользователь в бд
    def user_exist(self, id):
        with self.connection:
            result = self.cursor.execute('SELECT * FROM users WHERE id = ?', (id,)).fetchall()
            return bool(len(result))
    #получение всех пользователей
    def get_all_users(self):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM users ").fetchall()
            return(result)
    #запросы к статусу пользователя
    def get_status(self, id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM users WHERE id = ?", (id,)).fetchone()
            return(result[3])
    def update_status(self, id, status):
         with self.connection:
             return self.cursor.execute("UPDATE users SET status = ? WHERE id = ?", (status, id))

    #запросы к времени пользователя
    def get_time(self, id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM users WHERE id = ?", (id,)).fetchone()
            return(result[4])
    def update_time(self, id, time):
         with self.connection:
             return self.cursor.execute("UPDATE users SET time = ? WHERE id = ?", (time, id))

    #запросы к уровню пользователя
    def get_level(self, id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM users WHERE id = ?", (id,)).fetchone()
            return(result[1])
    def update_level(self, id, level):
         with self.connection:
             return self.cursor.execute("UPDATE users SET level = ? WHERE id = ?", (level, id))

    #запросы к счету пользователя
    def get_score(self, id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM users WHERE id = ?", (id,)).fetchone()
            return(result[2])
    def update_score(self, id, score):
         with self.connection:
             return self.cursor.execute("UPDATE users SET score = ? WHERE id = ?", (score, id))


    #запросы на эрудицию
    def get_erod_easy(self, number): #easy
        with self.connection:
            result = self.cursor.execute("SELECT * FROM easyerodition WHERE number = ?", (number,)).fetchone()
            return(result[1])
    def get_erod_answer_easy(self, number):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM easyerodition WHERE number = ?", (number,)).fetchone()
            return(result[2])
    def get_erod_medium(self, number): #medium
        with self.connection:
            result = self.cursor.execute("SELECT * FROM mediumerodition WHERE number = ?", (number,)).fetchone()
            return (result[1])
    def get_erod_answer_medium(self, number):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM mediumerodition WHERE number = ?", (number,)).fetchone()
            return(result[2])
    def get_erod_hard(self, number): #hard
        with self.connection:
            result = self.cursor.execute("SELECT * FROM harderodition WHERE number = ?", (number,)).fetchone()
            return (result[1])
    def get_erod_answer_hard(self, number):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM harderodition WHERE number = ?", (number,)).fetchone()
            return(result[2])


    # запросы на реакцию веществ
    def get_react_easy(self, number):
        with self.connection:
           result = self.cursor.execute("SELECT * FROM easyreaction WHERE number = ?", (number,)).fetchone()
           return(result[1])
    def get_react_answer_easy(self, number):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM easyreaction WHERE number = ?", (number,)).fetchone()
            return(result[2])
    def get_react_medium(self, number):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM mediumreaction WHERE number = ?", (number,)).fetchone()
            return (result[1])
    def get_react_answer_medium(self, number):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM mediumreaction WHERE number = ?", (number,)).fetchone()
            return (result[2])
    def get_react_hard(self, number):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM hardreaction WHERE number = ?", (number,)).fetchone()
            return (result[1])
    def get_react_answer_hard(self, number):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM hardreaction WHERE number = ?", (number,)).fetchone()
            return (result[2])

    # запросы к ОГЭ по химии
    def get_16task(self, number):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM OGE16 WHERE number = ?", (number,)).fetchone()
            return (result[1])
    def get_16task_answer(self, number):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM OGE16 WHERE number = ?", (number,)).fetchone()
            return (result[2])
    def get_18task(self, number):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM OGE18 WHERE number = ?", (number,)).fetchone()
            return (result[1])
    def get_18task_answer(self, number):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM OGE18 WHERE number = ?", (number,)).fetchone()
            return (result[2])
    def get_19task(self, number):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM OGE19 WHERE number = ?", (number,)).fetchone()
            return (result[1])
    def get_19task_answer(self, number):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM OGE19 WHERE number = ?", (number,)).fetchone()
            return (result[2])

    #запросы к ОГЭ по биологии
    def get_BIO_9task(self, number):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM BIO_OGE9 WHERE number = ?", (number,)).fetchone()
            return (result[1])
    def get_BIO_9task_answer(self, number):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM BIO_OGE9 WHERE number = ?", (number,)).fetchone()
            return (result[2])
    def get_BIO_17task(self, number):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM BIO_OGE17 WHERE number = ?", (number,)).fetchone()
            return (result[1])
    def get_BIO_17task_answer(self, number):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM BIO_OGE17 WHERE number = ?", (number,)).fetchone()
            return (result[2])
    def get_BIO_19task(self, number):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM BIO_OGE19 WHERE number = ?", (number,)).fetchone()
            return (result[1])
    def get_BIO_19task_answer(self, number):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM BIO_OGE19 WHERE number = ?", (number,)).fetchone()
            return (result[2])
    #получение всех учебных материалов
    def get_all_link(self):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM material ").fetchall()
            return(result)

    def close(self):
        self.connection.close()
