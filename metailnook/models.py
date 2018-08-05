# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class  account_profile(models.Model):
    name = models.CharField(max_length=100, verbose_name="name", unique=True)
    Company_name = models.CharField(max_length=100, verbose_name="Company_name")
    position = models.CharField(max_length=100, verbose_name="position")
    phone = models.IntegerField()
    Birthday = models.DateField(verbose_name="Birthday", null=True, default=None, blank=True)
    email = models.EmailField(verbose_name="Email")
    date_created = models.DateField(verbose_name="date_created", auto_now_add=True )

    def __str__(self):
        return self.name

class  staff(models.Model):
    name = models.CharField(max_length=100, verbose_name="name", unique=True)
    Company_name = models.CharField(max_length=100, verbose_name="Company_name")
    position = models.CharField(max_length=100, verbose_name="position")
    phone = models.IntegerField()
    Birthday = models.DateField(verbose_name="Birthday", null=True, default=None, blank=True)
    email = models.EmailField(verbose_name="Email")
    date_created = models.DateField(verbose_name="date_created", auto_now_add=True )

    def __str__(self):
        return self.name


class customer(models.Model):

    name = models.CharField(max_length=100, verbose_name="Name", unique=True)
    lastname = models.CharField(max_length=100, verbose_name="Last Name")
    address = models.CharField(max_length=100, verbose_name="address", null=True)
    date = models.DateField(verbose_name="date_created", auto_now_add=True)
    collectiondate = models.DateField(verbose_name="collectiondate", auto_now_add=False)

    def __str__(self):  # __unicode__ on Python 2
        return self.name

class blouse(models.Model):
    name = models.ForeignKey(customer)
    length = models.FloatField()
    bust = models.FloatField()
    shoulder = models.FloatField()
    waist = models.FloatField()
    neck = models.FloatField()
    halflength = models.FloatField()
    Quaterlength = models.FloatField()
    hip = models.FloatField()
    sleeve = models.FloatField()
    Rsleeve = models.FloatField()

    def __str__(self):  # __unicode__ on Python 2
        return str(self.name)





class skirt(models.Model):
    name = models.ForeignKey(customer)
    length = models.FloatField()
    halflength = models.FloatField()
    waist = models.FloatField()

    def __str__(self):  # __unicode__ on Python 2
        return str(self.name)


class sokoto(models.Model):
    name = models.ForeignKey(customer)
    length = models.FloatField()
    halflength = models.FloatField()
    bottom = models.FloatField()

    def __str__(self):  # __unicode__ on Python 2
        return str(self.name)


class gown(models.Model):
    name = models.ForeignKey(customer)
    length = models.FloatField()
    bust = models.FloatField()
    underburst = models.FloatField()
    shoulder = models.FloatField()
    waist = models.FloatField()
    halflength = models.FloatField()
    Quaterlength = models.FloatField()
    hip = models.FloatField()
    sleeve = models.FloatField()
    Rsleeve = models.FloatField()

    def __str__(self):  # __unicode__ on Python 2
        return str(self.name)


class caftan(models.Model):
    name = models.ForeignKey(customer)
    length = models.FloatField()
    underburst = models.FloatField()
    neck = models.FloatField()
    pocketline = models.FloatField()
    shoulder = models.FloatField()
    bust = models.FloatField()
    Quaterlength = models.FloatField()
    sleeve = models.FloatField()
    Rsleeve = models.FloatField()

    def __str__(self):  # __unicode__ on Python 2
        return str(self.name)

class shirt(models.Model):
    name = models.ForeignKey(customer)
    length = models.FloatField()
    collar = models.FloatField()
    neck = models.FloatField()
    chest = models.FloatField()
    shoulder = models.FloatField()
    back = models.FloatField()
    sleeve = models.FloatField()
    Rsleeve = models.FloatField()
    waist = models.FloatField()

    def __str__(self):  # __unicode__ on Python 2
        return str(self.name)


class buba(models.Model):
    name = models.ForeignKey(customer)
    length = models.FloatField()
    neck = models.FloatField()
    shoulder = models.FloatField()
    sleeve = models.FloatField()
    Rsleeve = models.FloatField()

    def __str__(self):  # __unicode__ on Python 2
        return str(self.name)


class suit(models.Model):
    name = models.ForeignKey(customer)
    length = models.FloatField()
    neck = models.FloatField()
    collar = models.FloatField()
    halflength = models.FloatField()
    burst = models.FloatField()
    shoulder = models.FloatField()
    armhole = models.FloatField()
    sleeve = models.FloatField()
    Rsleeve = models.FloatField()
    waist = models.FloatField()

    def __str__(self):  # __unicode__ on Python 2
        return str(self.name)

class trouser(models.Model):
    name = models.ForeignKey(customer)
    length = models.FloatField()
    waist = models.FloatField()
    tight = models.FloatField()
    roundkneel = models.FloatField()
    flap = models.FloatField()
    hip = models.FloatField()
    rSit = models.FloatField()
    bottom = models.FloatField()

    def __str__(self):  # __unicode__ on Python 2
        return str(self.name)


class payment(models.Model):
    name = models.ForeignKey(customer)
    bill = models.FloatField()
    advance = models.FloatField()
    balance = models.IntegerField(null=True)

    def __str__(self):  # __unicode__ on Python 2
        return str(self.name)


class navbar_link(models.Model):
    """docstring for navbar_link"""
    linkname = models.CharField(max_length=100, verbose_name="link name")
    link = models.CharField(max_length=100, verbose_name="link")
    icon = models.CharField(max_length=100, null=True)
    def __str__(self):  # __unicode__ on Python 2
        return self.linkname

        



