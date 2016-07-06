"""Ata urls."""

from django.conf.urls import url

from .views import Login, Index, SignUpStudent, Logout, Ata
urlpatterns = [
    url(r'^$', Index.as_view(), name="index"),
    url(r'^login/$', Login.as_view(), name="login"),
    url(r'^signupstudent/$', SignUpStudent.as_view(), name="create"),
    url(r'^signupteacher/$', SignUpStudent.as_view(), name="create"),
    url(r'^createuser/$', SignUpStudent.as_view(), name="post"),
    url(r'^logout/$', Logout.as_view(), name="logout"),
    url(r'^start_ata/$', Ata.as_view(), name="create"),
]
