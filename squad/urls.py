from django.conf.urls import url
from django.contrib import admin

from app.views import auth_views, squad_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # Authentication API
    url(r'^auth/register/?$', auth_views.register),
    url(r'^auth/login/?$', auth_views.login),
    url(r'^auth/me/?$', auth_views.get_auth_user),
    url(r'^auth/me/invites?$', squad_views.get_user_invites),

    # Squad API
    url(r'^squads/?$', squad_views.squads),
    url(r'^squad/join/?$', squad_views.join_squad),
    url(r'^squad/pins/?$', squad_views.pins),
    url(r'^squad/invites/?$', squad_views.get_squad_invites),

]
