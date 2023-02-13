from datetime import datetime

import sqlalchemy.exc
from project import db, ma
import uuid
import hashlib
import re


def emailValidator(email):
    if re.search("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+$", email):
        print('true mail')
        return True
    return False


def passwordValidator(password):
    if re.search("^(?=.*[a-zA-Z])|(?=.*\d).{8,}$", password):
        print('true pass')
        return True
    return False


class User(db.Model):
    __tablename__ = 'userList'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    firstname = db.Column(db.String(80), nullable=False)
    middlename = db.Column(db.String(80))
    lastname = db.Column(db.String(80), nullable=False)
    birthdate = db.Column(db.DateTime)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)

    def __repr__(self):
        return '<User(id: %r, username: %r, firstname: %r, middlename: %r, lastname: %r, birthdate: %r, email: %r, ' \
               'password: %r)> ' % (self.id, self.username, self.firstname, self.middlename, self.lastname,
                                    self.birthdate, self.email, self.password)

    @staticmethod
    def getUsers():
        users = User.query.all()
        result_list = user_schema.dump(users)
        return result_list

    @staticmethod
    def createUser(request):
        data = request.json
        try:
            if emailValidator(data['email']) and passwordValidator(data['password']):
                d = datetime.strptime(data['birthdate'], "%Y-%m-%d")
                d = d.date()
                salt = uuid.uuid4().hex
                hashed_passw = hashlib.sha256(salt.encode() + data['password'].encode()).hexdigest() + ':' + salt

                user = User(username=data['username'],
                            firstname=data['firstname'],
                            middlename=data['middlename'],
                            lastname=data['lastname'],
                            birthdate=d,
                            email=data['email'],
                            password=hashed_passw)
                db.session.add(user)
                db.session.commit()
                return {'message': 'User created successfully'}, 200
            else:
                return {'message': 'Wrong email or password format'}, 400
        except Exception as e:
            if isinstance(e, sqlalchemy.exc.IntegrityError):
                return {'message': 'User name already exists.'}, 500
            return {'message': 'Something went wrong'}, 500

    @staticmethod
    def deleteUser(username):
        user = User.query.filter_by(username=username).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return {'message': 'User deleted successfully'}, 200
        return {'message': 'Wrong username'}, 404

    @staticmethod
    def updateUser(request, username):
        data = request.json
        if emailValidator(data['email']) and passwordValidator(data['password']):
            user = User.query.filter_by(username=username).first()
            d = datetime.strptime(data['birthdate'], "%Y-%m-%d")
            d = d.date()
            salt = uuid.uuid4().hex
            hashed_passw = hashlib.sha256(salt.encode() + data['password'].encode()).hexdigest() + ':' + salt

            user.username = data['username'],
            user.firstname = data['firstname'],
            user.middlename = data['middlename'],
            user.lastname = data['lastname'],
            user.birthdate = d,
            user.email = data['email'],
            user.password = hashed_passw
            db.session.commit()
            return {'message': 'User updated successfully'}, 200
        else:
            return {'message': 'Wrong email format'}, 400


class OnlineUser(db.Model):
    __tablename__ = 'onlineUsers'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    ipaddress = db.Column(db.String(80), nullable=False)
    logindatetime = db.Column(db.DateTime)

    def __repr__(self):
        return '{\'id\': %r, \'username\': %r, \'ipaddress\': %r, \'logindatetime\': %r}' % (
            self.id, self.username, self.ipaddress, self.logindatetime)

    @staticmethod
    def getOnlineUsers():
        onlineUsers = OnlineUser.query.all()
        result_list = online_users_schema.dump(onlineUsers)
        return result_list

    @staticmethod
    def login(request):
        is_admin = False
        try:
            data = request.json
            user = User.query.filter_by(username=data['username']).first()
            if user.username == 'admin':
                is_admin = True
            hashedText, salt = user.password.split(':')

            if hashedText == hashlib.sha256(salt.encode() + data['password'].encode()).hexdigest():
                onlineUser = OnlineUser(username=user.username,
                                        ipaddress=request.remote_addr,
                                        logindatetime=datetime.now())
                db.session.add(onlineUser)
                db.session.commit()
                return {'message': 'Login successfully', 'isAdmin': is_admin}, 201
            else:
                return {'message': 'No user'}, 404
        except Exception as e:
            return {'message': 'No user'}, 404

    @staticmethod
    def logout(request):
        data = request.json
        onlineUser = OnlineUser.query.filter_by(username=data['username']).first()
        print(onlineUser)
        if onlineUser:
            db.session.delete(onlineUser)
            db.session.commit()
            return {'message': 'Logout successfully'}, 200
        return {'message': 'Wrong username'}, 404


class UserSchema(ma.Schema):
    class Meta:
        model = User
        fields = ('id', 'username', 'firstname', 'middlename', 'lastname', 'birthdate', 'email')


user_schema = UserSchema(many=True)


class onlineUsersSchema(ma.Schema):
    class Meta:
        model = OnlineUser
        fields = ('id', 'username', 'ipaddress', 'logindatetime')


online_users_schema = onlineUsersSchema(many=True)
