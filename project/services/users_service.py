from typing import Optional, List
from project.dao import UsersDAO
from project.exceptions import ItemNotFound
from project.models.models import User
from project.tools.security import AuthsService


class UsersService:
    def __init__(self, dao: UsersDAO) -> None:
        self.dao = dao

    def get_item(self, pk: int) -> User:
        if user := self.dao.get_by_id(pk):
            return user
        raise ItemNotFound(f'Director with pk={pk} not exists.')

    def get_all(self, page: Optional[int] = None) -> List[User]:
        return self.dao.get_all(page=page)
    
    def create_user(self, login, password):
        self.dao.create(login, password)
        
    def get_user_by_login(self, login):
        return self.dao.get_user_by_login(login)
        
    def chek(self, login, password):
        result = self.dao.get_user_by_login(login)
        if len(result):
            AuthsService().generate_tokens(login, password)
            
