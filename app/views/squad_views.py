from django.db import IntegrityError

from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from app.models import SquadUser
from app.services import squad_service


@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def create_squad(request):
    return Response({"message": "Success"}, status=status.HTTP_200_OK)


@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def join_squad(request):
    return Response({"message": "Success"}, status=status.HTTP_200_OK)