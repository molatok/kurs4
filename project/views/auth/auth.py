from flask_restx import Namespace, Resource
from flask import request
from project.container import user_service
from project.setup.api.models import user

api = Namespace('auth')

@api.route('/register')
class RegisterView(Resource):
    @api.marshal_with(user, as_list=True, code=200, description='OK')
    def post(self):
        data = request.json
        if data.get('email') and data.get('password'):
            return user_service.create_user(data.get('email'), data.get('password')), 201
        else:
            return "Не все поля заполнены", 401


@api.route('/login/')
class AuthView(Resource):
    @api.response(404, 'Not Found')
    @api.marshal_with(user, code=200, description='OK')
    def post(self):
        data = request.json
        if data.get('email') and data.get('password'):
            return user_service.chek(data.get('email'), ).data.get('password'), 201
        else:
            return "Не все поля заполнены", 401
