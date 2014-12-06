from django.conf.urls import patterns, include, url
from django.contrib import admin
from rentlet_user import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rentlet.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^login/$', views.user_login, name='user.user_login'),

)
