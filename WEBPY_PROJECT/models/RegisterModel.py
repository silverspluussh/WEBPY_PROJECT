from pymongo import MongoClient
import bcrypt


class RegisterModel:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.academy
        self.users = self.db.users

    def insert_users(self, data):
        hashing = bcrypt.hashpw(data.psword.encode(), bcrypt.gensalt())

        insert_id = self.users.insert({'name': data.name,
                                       'fullname': data.fullname,
                                       'email': data.email,
                                       'psword': hashing

                                       })
        print('id ', insert_id)
        find_user = self.users.find_one({"name": data.name})

        if bcrypt.checkpw("silverstone".encode(), find_user["psword"]):
            print("repeating password , please change it")
