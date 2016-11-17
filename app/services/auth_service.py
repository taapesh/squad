from rest_framework.authtoken.models import Token

from app.models import SquadUser


def register(email, username, password):
    user = SquadUser.objects.create_user(email=email, username=username, password=password)
    user.token = get_auth_token(user)
    return user


def get_all_users():
    return SquadUser.objects.all()


def get_auth_token(user):
    token = Token.objects.get_or_create(user=user)
    return token[0].key


def login(email, password):
    user = SquadUser.objects.get(email=email)
    if user.check_password(password):
        user.token = get_auth_token(user)
        return user
    else:
        return None