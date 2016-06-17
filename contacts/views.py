from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from wsgiref.util import FileWrapper

import os
import json


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
    final_list.sort()
    print final_list

     

    
    filename = "/tmp/export_{0}.csv".format(time.time())
    with open(filename, "wb") as f:
	row = []
        w = csv.writer(f)
        if "id" in headers:
            row.append('id')
        if "first_name" in headers:
            row.append("Vorname")
        if "last_name" in headers:
            row.append("Nachname")
        if "email" in headers:
	    row.append("EMail")
        w.writerow(row)


        for value in final_list:
	    row = []
            if "id" in headers:
	        row.append(value['id'])
            if "first_name" in headers:
	        row.append(value['first_name'])
            if "last_name" in headers:
	        row.append(value['last_name'])
            if "email" in headers:
	        row.append(value['email'])

            w.writerow(row)

    
    wrapper = FileWrapper(file(filename))
    response = HttpResponse(wrapper, content_type='text/csv')
    response['Content-Length'] = os.path.getsize(filename)
    response['Content-Disposition'] = 'attachment; filename="kontakte.csv"'
    return response

def get_groups(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        groups = Group.objects.filter(name__icontains = q)[:20]
        results = []
        for group in groups:
            group_json = {}
            group_json['id'] = group.id
            group_json['label'] = group.name
            group_json['value'] = group.name
            results.append(group_json)

        data = json.dumps(results)

    else:
        data = 'fail'

    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

def get_members(request):
    group_name = request.GET['group_name']
    print group_name

    gid = Group.objects.filter(name=group_name)[0].id
    member_list = User.objects.filter(group=gid)

    result = []
    for member in member_list:
        member_json = {}
	member_json['Vorname'] = str(member.first_name.encode('ascii', 'ignore').replace('"',"'" ))
	member_json['Nachname'] = str(member.last_name.encode('ascii', 'ignore').replace('"', '"'))
	member_json['EMail'] = str(member.email.encode('ascii', 'ignore').replace('"', '"'))
	result.append(member_json)
	
    result = json.dumps(result)
    return HttpResponse(result)

