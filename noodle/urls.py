from django.conf.urls import url
from . import views
#from django.contrib.auth.views import login, logout, logout_then_login
import django.contrib.auth.views as auth_views

urlpatterns = [
    url(r'^$', views.main_page, name='main_page'),
    #url(r'^login/$', views.login_page, name='login_page'),

    #login/logout urls
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^logout-then-login/$', auth_views.logout_then_login, name='logout_then_login'),
]

