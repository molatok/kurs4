from flask import request
from flask_restx import Namespace, Resource

from project.container import user_service
from project.setup.api.models import user

api = Namespace('user')


@api.route('/')
class RegisterView(Resource):
    @api.marshal_with(user, as_list=True, code=200, description='OK')
    def patch(self):
        data = request.json
        header = request.headers.environ.get('HTTP_AUTORIZATION').replace('Bearer ','')
        return user_service.update_user(data=data, refresh_token=header)

    @api.marshal_with(user, as_list=True, code=200, description='OK')
    def get(self):
        data = request.json
        header = request.headers.environ.get('HTTP_AUTORIZATION').replace('Bearer ','')
        return user_service.get_user_by_token(refresh_token=header)



@api.route('/password')
class AuthView(Resource):
    @api.response(404, 'Not Found')
    def put(self):
        data = request.json
        if data.get('access_token') and data.get('refresh_token'):
            return user_service.update(data.get('refresh_token')), 201
        else:
            return "Не все поля заполнены", 401
