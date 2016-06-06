from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'show_members', views.show_members, name='show_members'),
    url(r'details', views.details, name='details'),
    url(r'export_csv', views.export_csv, name='export_csv'),
]

