from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from wsgiref.util import FileWrapper

import os


import csv

import time
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
        if len(request.GET['searchterm']) <3:
            context = {
                'error': "Bitte mindestens drei Buchstaben",
            }
            return HttpResponse(template.render(context, request))
        member_list = User.objects.filter(first_name__contains=request.GET['searchterm'])
    else:
        member_list = tuple()

    context = {
        'user_list': member_list,
    }

    return HttpResponse(template.render(context, request))

def export_csv(request):
    headers = []
    output_data = {}
    wanted_data = {}
    final_list = []
    template = loader.get_template("contacts/user_detail.html")
    user_list = User.objects.filter(first_name__contains=request.GET['searchterm'])
#    if len(request.GET['searchterm']) <3:
#        context = {
#            'error': "Bitte mindestens drei Buchstaben",
#        }
#        return HttpResponse(template.render(context, request))
#
    for user in user_list:
        for key in user.__dict__.iteritems():
            wanted_data[key] = 'unselected'
    
    wanted_data['id'] = 'selected'
    wanted_data['first_name'] = 'selected'
    wanted_data['last_name'] = 'selected'
    wanted_data['email'] = 'selected'
    # Needs always be selected
 

    for key, value in wanted_data.iteritems():
        if value == 'selected':
            headers.append(key)

    for user in user_list:
        output_data[user.__dict__['id']] = []
        for key, value in user.__dict__.iteritems():
            if key in headers:
                output_data[user.__dict__['id']].append({key:value})



    for key, value in output_data.iteritems():
        tmp = dict()
        for my_dict_key in value:
            for key, value in my_dict_key.iteritems():
                tmp[key] = value
        final_list.append(tmp)
    print final_list
     

    filename = "/tmp/export_{0}.csv".format(time.time())
    with open(filename, "wb") as f:
        w = csv.DictWriter(f, fieldnames=headers)
        w.writeheader()
        for value in final_list:
            print value
            w.writerow(value) 

    
    wrapper = FileWrapper(file(filename))
    response = HttpResponse(wrapper, content_type='text/csv')
    response['Content-Length'] = os.path.getsize(filename)
    response['Content-Disposition'] = 'attachment; filename="kontakte.csv"'
    return response


