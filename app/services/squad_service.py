from rest_framework.authtoken.models import Token

from app.models import Pin, Squad, SquadUser, SquadInvite


def join_squad():
    pass


def create_squad(user, name, desc):
    squad = Squad.objects.create(leader=user, name=name, description=desc)
    user.squad = squad
    user.save()
    return squad


def create_squad_invite(squad, user_id, invited_by):
    user = SquadUser.objects.get(id=user_id)
    SquadInvite.objects.create(squad=squad, user=user, invited_by=invited_by)


def get_squad():
    pass


def create_pin(user, squad, title, desc, lat, lon, content_type, content_url):
    return Pin.objects.create(
        user=user,
        squad=squad,
        title=title,
        description=desc,
        lat=lat, lon=lon,
        content_type=content_type,
        content_url=content_url)


def get_pins_by_squad(squad):
    return Pin.objects.filter(squad=squad)


def create_squad_activity(squad):
    pass


def get_invites_by_user(user):
    return SquadInvite.objects.select_related("squad").filter(user=user)


def get_invites_by_squad(squad):
    return SquadInvite.objects.select_related("squad").filter(squad=squad)


def disband_squad(squad):
    pass