from django.db import IntegrityError

from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from app.models import SquadUser
from app.services import squad_service


@api_view(["GET", "POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def squads(request):
    if request.method == "GET":
        if request.user.squad:
            return Response(request.user.squad.to_json(), status=status.HTTP_200_OK)
        else:
            return Response({"message": "No squad for this user"}, status=status.HTTP_404_NOT_FOUND)
    else:
        if request.user.squad is not None:
            return Response({"message": "User is already part of a squad"}, status=status.HTTP_409_CONFLICT)

        name = request.data.get("name")
        desc = request.data.get("desc")

        squad = squad_service.create_squad(request.user, name, desc)

        invites = request.data.get("invites")
        for user_id in invites:
            squad_service.create_squad_invite(squad, user_id, request.user.username)

        return Response(squad.to_json(), status=status.HTTP_201_CREATED)



@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def join_squad(request):
    return Response({"message": "Success"}, status=status.HTTP_200_OK)


@api_view(["GET", "POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def pins(request):
    if request.method == "GET":
        pins = squad_service.get_pins_by_squad(request.user.squad)
        return Response([p.to_json() for p in pins.iterator()], status=status.HTTP_200_OK)
    else:
        user = request.user
        squad = request.user.squad

        if squad is None:
            return Response({"message": "User is not part of a squad"}, status=status.HTTP_404_NOT_FOUND)

        title = request.data.get("title")
        desc = request.data.get("desc")
        lat = request.data.get("lat")
        lon = request.data.get("lon")
        content_type = request.data.get("content_type")
        content_url = request.data.get("content_url")

        pin = squad_service.create_pin(user, squad, title, desc, lat, lon, content_type, content_url)
        return Response(pin.to_json(), status=status.HTTP_200_OK)


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def get_user_invites(request):
    invites = squad_service.get_invites_by_user(request.user)
    return Response([i.to_json() for i in invites.iterator()], status=status.HTTP_200_OK)


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def get_squad_invites(request):
    if request.user.squad is None:
        return Response({"message": "User is not part of a squad"}, status=status.HTTP_404_NOT_FOUND)

    invites = squad_service.get_invites_by_squad(request.user.squad)
    return Response([i.to_json() for i in invites.iterator()], status=status.HTTP_200_OK)

