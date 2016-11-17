from django.conf.urls import url
from django.contrib import admin

from app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # Authentication API
    url(r'^auth/register/?$', views.register),
    # url(r'^auth/login/?$', views.login),
]
