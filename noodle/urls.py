from django.conf.urls import url
from . import views
#from django.contrib.auth.views import login, logout, logout_then_login
import django.contrib.auth.views as auth_views
from noodlehouse.settings import VER

if VER == 'LAPSHOVPRO':
    urlpatterns = [
        url(r'^$', views.main_page, name='main_page'),
        # url(r'^blog/$', views.blog_page, name='blog_page'),
        # url(r'^one/$', views.one_page, name='one_page'),
        # url(r'^gallery/$', views.gallery_page, name='gallery_page'),
        # url(r'^video/$', views.video_page, name='video_page'),
        url(r'^photoshop/$', views.landing_page, name='landing_page'),
        #url(r'^login/$', views.login_page, name='login_page'),
    ]

elif VER == 'PROPORTRAIT':
    urlpatterns = [
        url(r'^$', views.one_page, name='main_page'),
    ]



    #login/logout urls
#     url(r'^login/$', auth_views.login, name='login'),
#     url(r'^logout/$', auth_views.logout, name='logout'),
#     url(r'^logout-then-login/$', auth_views.logout_then_login, name='logout_then_login'),