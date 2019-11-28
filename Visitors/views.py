# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from visitor_management import settings
from django.core.mail import send_mail
from twilio.rest import Client
from django_twilio.client import twilio_client
client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN) #REFER TO TWILIO DOCUMENTATION




# Create your views here.
def index(request):
    return render(request,'index.html') # GO TO INDEX.HTML
def display_visitors(request): # FUNCTION TO DISPLAY VISITORS
    items= Visitors.objects.all()
    context={
    'items':items,
    'header':'Visitor'
    }
    return render(request,'index.html',context) #USE TEMPLATE DEFINED IN INDEX.HTML TO DISPLAY CURRENT CONTEXT

def display_host(request): #FUNCTION TO DISPLAY HOSTS
    items= Host.objects.all()
    context={
    'items':items,
    'header':'Host'
    }
    return render(request,'index.html',context) #USE TEMPLATE DEFINED IN INDEX.HTML TO DISPLAY CURRENT CONTEXT



def add_visitor(request): # FUNCTION TO ADD A NEW VISITOR

    if request.method=='POST': 
        form=VisitorForm(request.POST) 
        if form.is_valid():
            instance=form.save()     # SAVE DATA IF VALID
            sendmailtohost(instance) # PASS VALUE OF CURRENTLY CREATED VISITOR TO EMAIL FUNCTION
            sendsmstohost(instance)  # PASS VALUE OF CURRENTLY CREATED VISITOR TO SMS FUNCTION




        return redirect('index') # REDIRECT TO INDEX.HTML UPON SUCCESSFUL COMPLETION


    else:
        form=VisitorForm()
        return render(request,'add_new.html',{'form':form})  # RETURNS HTTP RESPONSE OBJECT WITH THE TEMPLATE SPECIFIED IN ADD_NEW.HTML AND TAKES IN FORM AS CONTEXT

def add_host(request): # FUNCTION TO ADD HOST
    if request.method=='POST': 
        form=HostForm(request.POST)
        if form.is_valid():
            instance=form.save() # SAVE DATA IF VALID


            return redirect('index') # REDIRECT TO INDEX.HTML
    else:
        form=HostForm()
        return render(request,'add_new.html',{'form':form}) #RETURNS HTTP RESPONSE OBJECT WITH THE TEMPLATE SPECIFIED IN ADD_NEW.HTML AND TAKES IN FORM AS CONTEXT


def edit_item(request, pk, model, cls): #GENERALIZED METHOD INHERITED BY EDIT_VISITOR AND EDIT_HOST FUNCTIONS
    item = get_object_or_404(model, pk=pk)

    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            ins=form.save()
            sendmailtovisitor(ins) #PASS CURRENTLY EDITED OBJECT TO MAIL FUNCTION
            sendsmstovisitor(ins) #PASS CURRENTLY EDITED OBJECT TO SMS FUNCTION
            return redirect('index')
    else:
        form = cls(instance=item)

        return render(request, 'edit_item.html', {'form': form})
def edit_visitor(request, pk): # PK IS THE AUTO GENERATED PRIMARY KEY BY THE DJANGO FRAMEWORK PASSED AS ARGUMENT TO GET THE PARTICULAR OBJECT TO BE EDITED
    return edit_item(request, pk, Visitors, VisitorForm)


def sendmailtohost(instance): # EMAIL FUNCTION TO SEND EMAIL TO HOST UPON HAVING A NEW VISITOR
      subject="New Visitor"
      to='HOST_EMAIL_ID' # EMAIL ID OF HOST
      message='\n Name: '+instance.name+'\n Email: '+instance.email+'\n Phone: '+instance.phone+'\n Checkin: '+str(instance.checkin)
      send_mail(subject,message,settings.EMAIL_USER,[to,]) # IMPORTS EMAIL OF SITE MANAGER IN THE 'FROM' FIELD

def sendmailtovisitor(instance): # EMAIL FUNCTION TO SEND EMAIL TO VISITOR AFTER HIS EXIT
    subject="Visit Details" 
    message='\n Name: '+instance.name+'\n Email: '+instance.email+'\n Phone: '+instance.phone+'\n'+' Checkin: '+ str(instance.checkin)+'\n Checkout: '+ str(instance.checkout)+'\n Host name: '+ settings.HOST_NAME+'\n Address: '+settings.HOST_ADDRESS # HOST NAME AND ADDRESS IS HARDCODED IN THE SETTINGS.PY FILE
    send_mail(subject,message,settings.EMAIL_USER,[instance.email,]) # IMPORTS EMAIL OF SITE MANAGER IN THE 'FROM' FIELD

def sendsmstohost(instance): # SEND SMS TO HOST WHEN A NEW VISITOR ENTERS
    r=twilio_client.messages.create(
    to='HOST_PHONE_NUMBER', # HOST'S PHONE NUMBER
    from_='SITE_MANAGER_NUMBER',# SITE MANAGER'S NUMBER 
    body='\n Name: '+instance.name+'\n Email: '+instance.email+'\n Phone: '+instance.phone+'\n Checkin: '+str(instance.checkin))
    if(r):
        print('success') # PRINT SUCCESS IN CONSOLE UPON SUCCESSFUL DELIVERY OF THE MESSAGE 

def sendsmstovisitor(instance):
    m=twilio_client.messages.create(
    to=instance.phone,           #PHONE NUMBER OF CURRENT VISITOR RETRIEVED FROM THE DATABASE
    from_='SITE_MANAGER_NUMBER', #SITE MANAGER'S NUMBER
    body='\n Name: '+instance.name+'\n Email: '+instance.email+'\n Phone: '+instance.phone+'\n Checkin: '+str(instance.checkin)+'\n Checkout: '+ str(instance.checkout)+'\n Host name: '+ settings.HOST_NAME+'\n Address: '+settings.HOST_ADDRESS)
    if(m):
        print('success') #PRINT SUCCESS IN CONSOLE UPON SUCCESSFUL DELIVERY OF THE MESSAGE
