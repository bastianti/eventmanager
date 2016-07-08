from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'show_members', views.show_members, name='show_members'),
    url(r'details', views.details, name='details'),
    url(r'export_csv', views.export_csv, name='export_csv'),
    url(r'get_grouplist', views.get_grouplist, name='get_grouplist'),
    url(r'get_memberlist', views.get_memberlist, name='get_memberlist'),
    url(r'get_members', views.get_members, name='get_members'),
    url(r'get_user', views.get_user, name='get_user'),
    url(r'send_invite', views.send_invite, name='send_invite'),
]

