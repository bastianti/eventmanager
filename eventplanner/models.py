from __future__ import unicode_literals

from django.db import models

class Event(models.Model):
    title    = models.CharField(max_length=30)
    date     = models.DateField()
    location = models.CharField(max_length=100)
    owner    = models.CharField(max_length=100)
    text     = models.TextField()
    def __str__(self):
        return self.title
    

class User_Invite(models.Model):
    tn_status  = (
                   ('+', 'Teilnahme'),
                   ('0', 'Unklar'),
                   ('-', 'Absage'),
                 )
    tnstatus  = models.CharField(max_length=100, choices=tn_status, default='0')
    user      = models.ForeignKey('contacts.User', blank=True)
    event     = models.ForeignKey('Event')
    user_hash = models.CharField(max_length=30)
