from django.conf.urls import url
from . import views
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^login/$',views.user_login,name='user_login'),
    #url(r'^login/$',auth_views.LoginView.as_view(template_name='account/login2.html'),name='user_login'),  #django2以上版本使用方式修改为这种模式，与pdf教材有异
    url(r'^new-login/$',auth_views.LoginView.as_view(template_name='account/login.html')),
    #url(r'^logout/$',auth_views.LogoutView.as_view(template_name='registration/logged_out.html'),name='user_logout'),
    url(r'^logout/$',auth_views.LogoutView.as_view(template_name='account/logout.html'),name='user_logout'),
    url(r'^register/$',views.register,name='user_register'),
]