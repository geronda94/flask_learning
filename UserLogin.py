from flask import url_for
from flask_login import UserMixin


class UserLogin(UserMixin):
    def fromDB(self,  user_id, db):
        self.__user = db.getUser(user_id)
        return self

    def create(self, user):
        self.__user = user
        print(user)
        return self

    def get_id(self):
        res = str(self.__user['id'])
        print(res)
        return res

    def getName(self):
        res=str(self.__user['name'] if self.__user['name'] else "Без имени")
        return res


    def getEmail(self):
        res = str(self.__user['email'] if self.__user['email'] else "Без имени")
        print(res)
        return res

    def getAvatar(self, app):
        img = None
        if not self.__user['avatar']:
            try:
                with app.open_resource(app.root_path + url_for('static', filename='images/default.png'), 'rb') as f:
                    img = f.read()
            except FileNotFoundError as e:
                print('Не найдена аватарка по умолчанию'+str(e))

        else:
            img = self.__user['avatar']
        return img



    def verifyExt(self, filename):
        ext = filename.rsplit('.',1)[1]
        if ext == 'png' or ext=='PNG' or ext =='jpg' or ext=='JPG':
            return True
        else:
            return False


    # def is_authenticated(self):
    #     return True
    #
    # def is_active(self):
    #     return True
    #
    #
    # def is_anonimous(self):
    #     return False

