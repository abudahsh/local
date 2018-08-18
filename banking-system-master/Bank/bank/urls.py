from django.conf.urls.defaults import *


urlpatterns = patterns('',
	#url(r'^$', 'bank.view.home'),
	url(r'^transfer/$', 'bank.views.transfer'),
	url(r'^view/(\d+)$', 'bank.views.viewMoney'),
	url(r'^create/$', 'bank.views.create_account'),
	url(r'^$', 'bank.views.homepage')
)

