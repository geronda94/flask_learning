import math
import re
import sqlite3
import time

from flask import url_for


class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def getMenu(self):
        sql = '''SELECT * FROM mainmenu;'''
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res
        except:
            print('Ошибка чтения из БД')
        return []

    def addPost(self, title, text, url):
        try:
            self.__cur.execute(f"SELECT COUNT()  as 'count' FROM posts WHERE url='{url}';")
            res = self.__cur.fetchone()
            if res['count']> 0:
                print('Статья с таким url уже существует')
                return False
            #Замена пути до картинки черз регулярные выражения
            base = url_for('static', filename='images_html')
            text = re.sub(r"(?P<tag><img\s+[^>]*src=)(?P<quote>[\"'])(?P<url>.+?)(?P=quote)>",
                          "\\g<tag>" + base + "/\\g<url>", text)

            tm = math.floor(time.time())
            self.__cur.execute("INSERT INTO posts VALUES(NULL, ?, ?, ?, ?)", (title, text, url, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print('Ошибка добавления статьи в ДБ во время записи' + str(e))
            return False

        return True

    def getPost(self, alias):
        try:
            self.__cur.execute(f"SELECT title, text FROM posts WHERE url LIKE '{alias}' LIMIT 1;")
            res = self.__cur.fetchone()
            if res:
                return res

        except sqlite3.Error as e:
            print('Ошибка извлечения статьи из ДБ во ' + str(e))

        return (False, False)

    def getPostAnonce(self):
        try:
            self.__cur.execute(f"SELECT id, title, url, text FROM posts ORDER BY time DESC;")
            res = self.__cur.fetchall()
            if res:
                return res

        except sqlite3.Error as e:
            print('Ошибка извлечения статей из ДБ  ' + str(e))

        return []

    def addUser(self, name, email, password):
        tm = math.floor(time.time())
        try:
            self.__cur.execute(f"SELECT COUNT() as 'count' FROM users WHERE email LIKE '{email}'")
            res = self.__cur.fetchone()
            if res['count'] > 0:
                print('ПОльзователь с таким email уже существует')
                return False

            self.__cur.execute(f"INSERT INTO users VALUES(NULL, ?, ?, ?, NULL, ?)", (name, email, password, tm))
            self.__db.commit()

        except sqlite3.Error as e:
            print('Ошибка добавления статьи в ДБ во время записи' + str(e))
            return False

        return True


    def getUser(self, user_id):
        try:
            self.__cur.execute(f"SELECT * FROM users WHERE id='{user_id}' LIMIT 1")
            res = self.__cur.fetchone()
            if not res:
                print('Пользователь не найден')
                return False

            return res

        except sqlite3.Error as ex:
            print(f'Ошибка при получени данных из БД {ex}')
            return False

    def  getUserByEmail(self, email):
        try:
            self.__cur.execute(f"SELECT * FROM users WHERE email='{email}' LIMIT 1")
            res = self.__cur.fetchone()
            if not res:
                print('Пользователь не найден')
                return False

            return res
        except sqlite3.Error as e:
            print('Ошибка  получения данных из БД', + str(e))

        return False


    def getUserInfo(self, id):
        try:
            self.__cur.execute(f"SELECT * FROM users WHERE id='{id}' LIMIT 1;")
            res = self.__cur.fetchone()
            if not res:
                print('Пользователь не найден')
                return False
            else:
                return (res['name'], res['email'])

        except sqlite3.Error as e:
            print('Ошибка  получения данных из БД', + str(e))

        return False
