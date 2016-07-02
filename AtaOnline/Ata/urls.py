"""Ata urls."""

from django.conf.urls import url
from .views import Login, Index, SignUp, Logout
urlpatterns = [
    url(r'^$', Index.as_view(), name="index"),
    url(r'^login/$', Login.as_view(), name="login"),
    url(r'^signup/$', SignUp.as_view(), name="create"),
    url(r'^createuser/$', SignUp.as_view(), name="post"),
    url(r'^logout/$', Logout.as_view(), name="logout"),
]
