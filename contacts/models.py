# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class User(models.Model):
    sex_choice      = (
                         ('M', 'Männlich'), 
                         ('W', 'Weiblich')
                      )
 
    def user_directory_path(instance, filename):
        return 'user_{0}/{1}_{2}'.format(instance.user.first_name, instance.user.last_name, filename)


    first_name      = models.CharField("Vorname", max_length=30)
    second_name     = models.CharField("Zweiter Vorname", max_length=30, blank=True)
    last_name       = models.CharField("Nachname", max_length=30)
    sex             = models.CharField("Geschlecht", max_length=1, choices=sex_choice)
    birthday        = models.DateField("Geburtstag")
    juleica_date    = models.DateField("Juleica Datum", blank=True, null=True) 
    first_aid_date  = models.DateField("Erste Hilfe Datum", blank=True, null=True)
    einsegnung_date = models.DateField("Einsegnung Datum", blank=True, null=True)
    nc_year         = models.PositiveSmallIntegerField("Newcomer Jahrgang", blank=True, null=True)
    landline        = models.CharField("Festnetz Telefon", max_length=15, blank=True)
    mobilephone     = models.CharField("Handy", max_length=20, blank=True)
    facebook_link   = models.CharField("Facebook Link", max_length=100, blank=True)
    first_commway   = models.ForeignKey('Commways', verbose_name="Kommunikationsweg")
    email           = models.EmailField("EMail")
    group           = models.ManyToManyField('Group', verbose_name="Gruppen")
    picture         = models.ImageField("Bild", upload_to='pictures/', blank=True)
    picture_date    = models.DateField("Bilddatum", blank=True, null=True)
    street          = models.CharField("Straße", max_length=30)
    street_no       = models.PositiveSmallIntegerField("Hausnummer")
    zipcode         = models.PositiveSmallIntegerField("Postleitzahl")
    city            = models.CharField("Stadt", max_length=30)
    addition        = models.CharField("Adresszusatz", max_length=100, blank=True)

    def __str__(self):
        return "{0} {1}".format(self.first_name, self.last_name)

class Commways(models.Model):
    way             = models.CharField(max_length=21) 
    def __str__(self):
        return self.way
