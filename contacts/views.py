from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Group, User, Commways



def index(request):
    return HttpResponse("Nothing to see here")

def show_members(request):
     template = loader.get_template("contacts/show_members.html")
     member_list = ["No Members"]
     if request.GET:
         gid = Group.objects.filter(name=request.GET['group'])[0].id
         member_list = User.objects.filter(group=gid)
     group_list = Group.objects.all()
     context = {
         'group_list': group_list,
         'member_list': member_list
     } 
     return HttpResponse(template.render(context, request))

def details(request):
    template = loader.get_template("contacts/user_detail.html")

    if 'searchterm' in request.GET:
        member_list = User.objects.filter(first_name__contains=request.GET['searchterm'])
    else:
        member_list = tuple()

    context = {
        'user_list': member_list,
    }

    return HttpResponse(template.render(context, request))
