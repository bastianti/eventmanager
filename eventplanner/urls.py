from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.plan_event, name='plan_event'),
    url(r'create_invite', views.create_invite, name='create_invite'),
]

