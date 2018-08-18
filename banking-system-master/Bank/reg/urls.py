from django.conf.urls.defaults import *

url patterns=patterns('',
    url(r'^login/$', 'reg.views.loginView'),
    url(r'^logout/$', 'reg.views.logoutView'),
)
