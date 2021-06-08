#!/usr/local/bin/python
import web
from models import RegisterModel,LoginModel

web.config.debug = False

url = ('/', 'Home',
       '/register', 'Register',
       '/login', 'Login',
       '/logout', 'Logout',
       '/postregistration', 'PostRegistration',
       '/login_checker', "LoginChecker"

       )


app = web.application(url, globals())
session = web.session.Session(app, web.session.DiskStore("sessions"), initializer={'user': None})
session_data = session._initializer

render = web.template.render("Templates", base="mainlayout", globals={'session':session_data, 'current_user': session_data['user']})


class Home:
    def GET(self):
        data = type('obj', (object, ), {'email':'silverstone843@yahoo.com','psword': 'silverstone'})

        logging = LoginModel.LoginModel()
        IsRight = logging.check_users(data)

        if IsRight:
            session_data['user'] = IsRight

        return render.home()


class Register:
    def GET(self):
        return render.register()


class Login:
    def GET(self):
        return render.login()


class LoginChecker:
    def POST(self):
        data = web.input()
        log_model = LoginModel.LoginModel()
        IsRight = log_model.check_users(data)

        if IsRight:
            session_data['user'] = IsRight
            return IsRight


class PostRegistration:
    def POST(self):
        data = web.input()
        reg_model = RegisterModel.RegisterModel()
        reg_model.insert_users(data)

        return data.fullname


class Logout:
    def GET(self):
        session['user'] = None
        session_data['user'] = None

        session.kill()
        return 'success'


if __name__ == "__main__":
    app.run()
