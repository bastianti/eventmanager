from __future__ import unicode_literals

from django.db import models

class Event(models.Model):
    title    = models.CharField(max_length=30)
    date     = models.DateField()
    location = models.CharField(max_length=100)
    owner    = models.CharField(max_length=100)
    def __str__(self):
        return self.title
    

class Invite(models.Model):
    tn_status = (
                    ('+', 'Teilnahme'),
	            ('0', 'Unklar'),
	            ('-', 'Absage'),
                )

    tnstatus = models.CharField(max_length=1, choices=tn_status, default='0')
    text     = models.TextField()
    groups   = models.ManyToManyField('contacts.Group', blank=True)
    user     = models.ManyToManyField('contacts.User', blank=True)
    event    = models.ForeignKey('Event')

    def __str__(self):
        return str(self.event)
