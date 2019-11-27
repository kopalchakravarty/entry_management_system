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
client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)




# Create your views here.
def index(request):
    return render(request,'index.html')
def display_visitors(request):
    items= Visitors.objects.all()
    context={
    'items':items,
    'header':'Visitor'
    }
    return render(request,'index.html',context)

def display_host(request):
    items= Host.objects.all()
    context={
    'items':items,
    'header':'Host'
    }
    return render(request,'index.html',context)



def add_visitor(request):

    if request.method=='POST':
        form=VisitorForm(request.POST)
        if form.is_valid():
            instance=form.save()
            sendmailtohost(instance)
            sendsmstohost(instance)


        #@receiver(post_save,sender='Visitors.Visitors')


        return redirect('index')


    else:
        form=VisitorForm()
        return render(request,'add_new.html',{'form':form})

def add_host(request):
    if request.method=='POST':
        form=HostForm(request.POST)
        if form.is_valid():
            instance=form.save()


            return redirect('index')
    else:
        form=HostForm()
        return render(request,'add_new.html',{'form':form})


def edit_item(request, pk, model, cls):
    item = get_object_or_404(model, pk=pk)

    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            ins=form.save()
            sendmailtovisitor(ins)
            sendsmstovisitor(ins)
            return redirect('index')
    else:
        form = cls(instance=item)

        return render(request, 'edit_item.html', {'form': form})
def edit_visitor(request, pk):
    return edit_item(request, pk, Visitors, VisitorForm)
def edit_host(request,pk):
    return edit_item(request,pk,Host,HostForm)

def sendmailtohost(instance):
      subject="New Visitor"
      to='CEO@gmail.com' #EMAIL ID OF HOST
      message='\n Name: '+instance.name+'\n Email: '+instance.email+'\n Phone: '+instance.phone+'\n Checkin: '+str(instance.checkin)
      send_mail(subject,message,settings.EMAIL_USER,[to,])

def sendmailtovisitor(instance):
    subject="Visit Details"
    message='\n Name: '+instance.name+'\n Email: '+instance.email+'\n Phone: '+instance.phone+'\n'+' Checkin: '+ str(instance.checkin)+'\n Checkout: '+ str(instance.checkout)+'\n Host name: '+ settings.HOST_NAME+'\n Address: '+settings.HOST_ADDRESS
    send_mail(subject,message,settings.EMAIL_USER,[instance.email,])

def sendsmstohost(instance):
    r=twilio_client.messages.create(
    to='+919826680561', #HOST'S PHONE NUMBER
    from_='+1 323 815 7836',# SITE MANAGER'S NUMBER 
    body='\n Name: '+instance.name+'\n Email: '+instance.email+'\n Phone: '+instance.phone+'\n Checkin: '+str(instance.checkin))
    if(r):
        print('success')

def sendsmstovisitor(instance):
    m=twilio_client.messages.create(
    to=instance.phone,
    from_='+1 323 815 7836', #SITE MANAGER'S NUMBER
    body='\n Name: '+instance.name+'\n Email: '+instance.email+'\n Phone: '+instance.phone+'\n Checkin: '+str(instance.checkin)+'\n Checkout: '+ str(instance.checkout)+'\n Host name: '+ settings.HOST_NAME+'\n Address: '+settings.HOST_ADDRESS)
    if(m):
        print('success')
