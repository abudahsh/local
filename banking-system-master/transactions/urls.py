from django.conf.urls import url

from .views import diposit_view, withdrawal_view

urlpatterns = [
    # url(r'^$', home_view, name='home'),
    url(r'^deposit/$', diposit_view),
    url(r'^withdrawal/$', withdrawal_view),
]
