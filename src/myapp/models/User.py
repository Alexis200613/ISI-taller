from .RoleType import RoleType
from .Question import Question
from .Response import Response

class User:

    def __init__(self, username: str, email: str, password: str, role: RoleType, id: int):
        self._username = username
        self._email = email
        self._password = password
        self._role = role
        self.id = id

    def get_username(self):
        return self._username

    def get_role(self):
        return self._role

    def get_id(self):
        return self._id

    def ask(question: Question):
        
        # TODO: implementar ask. Deberia postearse a una lista de preguntas?
        return

    def respond(question: Question, response: Response):
        question.add_response(response)