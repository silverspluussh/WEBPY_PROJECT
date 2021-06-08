from pymongo import MongoClient
import bcrypt


class LoginModel:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.academy
        self.users = self.db.users

    def check_users(self,data):
        a_user = self.users.find_one({'email': data.email})

        if a_user:
            if bcrypt.checkpw(data.psword.encode(), a_user['psword']):
                return a_user
            else:
                return False




