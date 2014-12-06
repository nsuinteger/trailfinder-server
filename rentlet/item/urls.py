from django.conf.urls import patterns, include, url
from django.contrib import admin
from item import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rentlet.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^list/$', views.item_list, name='item.item_list'),

)
