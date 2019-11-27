# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from visitor_management import settings


# Create your models here.
class BasicInfo(models.Model):                      # CREATING TEMPLATE OF OUR MODELS
    name=models.CharField(max_length=30,blank=False)
    phone=models.CharField(max_length=20,blank=False)
    email=models.CharField(max_length=40)
    class Meta:
        abstract=True                             # WILL NOT BE CREATED AS A SEPARATE MODEL 


    def str(self):
        return 'Name:{0} Phone:{1}'.format(self.name,self.phone)

class Visitors(BasicInfo):             # MODEL VISITORS INHERITS TEMPLATE FROM BASICINFO
    pass
    checkin=models.DateTimeField(default=datetime.now,blank=False)  #ADDED CHECKIN CHECKOUT FIELDS 
    checkout=models.DateTimeField(blank=True, null=True)

class Host(BasicInfo):              # MODEL HOST INHERITS TEMPLATE FROM BASICINFO
    pass
