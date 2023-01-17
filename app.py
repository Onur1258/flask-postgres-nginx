from flask import request
from flask_restful import Resource, Api
from project import createApp
from project.initialize_db import createDB
from project.models import User, OnlineUser
import subprocess
from flask import jsonify

app = createApp()
db = createDB(app)
api = Api(app)


class UserCreate(Resource):
    def post(self):
        return User.createUser(request=request)


class UserDelete(Resource):
    def delete(self, username):
        return User.deleteUser(username=username)


class UserUpdate(Resource):
    def put(self, username):
        return User.updateUser(request=request, username=username)


class UserList(Resource):
    def get(self):
        return User.getUsers()


class OnlineUsers(Resource):
    def get(self):
        return OnlineUser.getOnlineUsers()


class Login(Resource):
    def post(self):
        return OnlineUser.login(request=request)


class Logout(Resource):
    def delete(self):
        return OnlineUser.logout(request=request)


class GetLogs(Resource):
    def get(self):
        try:
            strA = ""
            with open('/var/log/nginx/access.log', "r") as file:
                strA += file.read()

            return jsonify({'Logs': strA})
        except:
            return jsonify({'message': 'sıkıntı'})


api.add_resource(UserCreate, '/user/create')
api.add_resource(UserDelete, "/user/delete/<string:username>")
api.add_resource(UserUpdate, '/user/update/<string:username>')
api.add_resource(UserList, '/user/list')
api.add_resource(OnlineUsers, '/onlineusers')
api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout')
api.add_resource(GetLogs, '/logs')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
