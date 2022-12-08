from flask import request
from flask_restx import Namespace, Resource
from project.container import user_service
from project.setup.api.models import user
from project.setup.api.parsers import page_parser
from project.tools.decorators import auth_required
from project.tools.security import user_token_by_email

api = Namespace('user')


@api.route('/', methods=['GET', 'PATCH'])
class RegisterView(Resource):
    @api.expect(page_parser)
    @api.marshal_with(user, as_list=True, code=200, description='OK')
    def get(self):
        return user_service.get_all(**page_parser.parse_args())
    
    @auth_required
    def patch(self):
        token = request.headers["Authorization"].split("Bearer ")[-1]
        user_up = request.json
        email = user_token_by_email(token)
        return user_service.update_user(email, user_up), 201


@api.route('/password/', methods=['PUT'])
class ChangepasswView(Resource):
    @auth_required
    def put(self):
        token = request.headers["Authorization"].split("Bearer ")[-1]
        data_passwords = request.json
        if data_passwords:
            return user_service.update_password(token, data_passwords), 201
        return "", 401
