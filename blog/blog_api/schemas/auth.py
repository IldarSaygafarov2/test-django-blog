from ninja import Schema
from datetime import datetime
# схема для авторизации
# username, password

class UserLoginSchema(Schema):
    username: str
    password: str


class UserRegistrationSchema(Schema):
    username: str
    email: str
    first_name: str
    password1: str
    password2: str


class UserOutSchema(Schema):
    id: int
    username: str
    email: str
    first_name: str
    date_joined: datetime

# схема для регистрации
# username, email, first_name, password1, password2