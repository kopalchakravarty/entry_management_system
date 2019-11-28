from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^display_visitors$',display_visitors,name="display_visitors"),
    url(r'^display_host$',display_host,name="display_host"),
    url(r'^add_visitor$',add_visitor,name="add_visitor"),
    url(r'^add_host$',add_host,name="add_host"),
    



    ]
