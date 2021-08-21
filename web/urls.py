from django.conf.urls import url
from web.views import account
from web.views import home
from django.urls import path
from web.views import videocapture


urlpatterns = [
    # 注册登陆
    url(r'^register/$', account.register, name='register'),
    url(r'^login/sms/$', account.login_sms, name='login_sms'),
    url(r'^login/$', account.login, name='login'),
    url(r'^image/code/$', account.image_code, name='image_code'),
    url(r'^send/sms/$', account.send_sms, name='send_sms'),
    url(r'^logout/$', account.logout, name='logout'),
    url(r'^index/$', home.index, name='index'),
    # 界面一
    url(r'^concentration/$', account.concentration, name='concentration'),
    url(r'^concentration/issues/chart/$', account.issues_chart, name='issues_chart'),
    url(r'^concentration/issues/priority/$', account.issues_priority, name='issues_priority'),
    url(r'^concentration/issues/barchart/$', account.issues_barchart, name='issues_barchart'),
    # 界面二
    url(r'^administration/0$', account.administration0, name='administration_0'),
    url(r'^administration/1$', account.administration1, name='administration_1'),
    url(r'^administration/2$', account.administration2, name='administration_2'),

    # path('', videocapture.home),
    url('getVideo', videocapture.getVideo)

]
