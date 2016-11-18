from django.db import IntegrityError

from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from app.models import SquadUser
from app.services import auth_service


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def get_auth_user(request):
    return Response(request.user.to_json(), status=status.HTTP_200_OK)


@api_view(["POST"])
def register(request):
    email = request.data.get("email")
    username = request.data.get("username")
    password = request.data.get("password")

    try:
        user = auth_service.register(email, username, password)
        auth_service.get_auth_token(user)
        return Response(user.to_json(), status=status.HTTP_201_CREATED)
    except IntegrityError:
        return Response({"message": "That email is already in use"}, status=status.HTTP_409_CONFLICT)


@api_view(["POST"])
def login(request):
    email = request.data.get("email")
    password = request.data.get("password")

    try:
        user = auth_service.login(email, password)
        if (user is not None):
            return Response(user.to_json(), status=status.HTTP_200_OK)
        else:
            return Response({"message": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
    except SquadUser.DoesNotExist:
        return Response({"message": "Not found"}, status=status.HTTP_404_NOT_FOUND)
