from project import createApp
from project.backend.initialize_db import createDB
from flask_restful import Api
from project.controller.ClientApi import *

app = createApp()
db = createDB(app)
api = Api(app)

api.add_resource(Home, '/')
api.add_resource(SignUp, '/signup'),
api.add_resource(UserPage, '/spectacular/page')
api.add_resource(ODPage, '/adminOD')


api.add_resource(UserCreate, '/user/create')
api.add_resource(UserDelete, "/user/delete/<string:username>")
api.add_resource(UserUpdate, '/user/update/<string:username>')
api.add_resource(UserList, '/user/list')
api.add_resource(OnlineUsers, '/onlineusers')
api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout')
api.add_resource(GetLogs, '/logs')


