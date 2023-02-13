import json
from flask import request, render_template, make_response
from flask_restful import Resource
from project.backend.models import *
from flask import jsonify

headers_html = {'Content-Type': 'text/html'}
headers_json = {'Content-Type': 'application/json'}


class Home(Resource):
    def get(self):
        return make_response(render_template('index.html'), 200,
                             headers_html)


class SignUp(Resource):
    def get(self):
        return make_response(render_template('signup.html'), 200, headers_html)


class UserPage(Resource):
    def get(self):
        return make_response(render_template('user.html'), 200, headers_html)


class ODPage(Resource):
    def get(self):
        return make_response(render_template('od.html'), 200, headers_html)


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
        users = User.getUsers()
        return users


class OnlineUsers(Resource):
    def get(self):
        online_users = OnlineUser.getOnlineUsers()
        return make_response(json.dumps(online_users), 200,
                             headers_json)


class Login(Resource):
    def post(self):
        message, status = OnlineUser.login(request=request)
        return make_response(message, status, headers_json)


class Logout(Resource):
    def delete(self):
        return OnlineUser.logout(request=request)


class GetLogs(Resource):
    def get(self):
        try:
            strA = ""
            with open('/var/log/nginx/access.log', "r") as file:
                strA += file.read()

            return json.dumps({'Logssssssss': strA})
        except:
            return jsonify({'message': 'sikinti'})
