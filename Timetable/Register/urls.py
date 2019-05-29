from django.conf.urls import url
from . import views




urlpatterns = [

    url(r'^$', views.login),

    url(r'^register', views.register),

    url(r'^reg', views.Reg),

    url(r'^logged', views.login),

   # url(r'^logged', views.loginconfirm),

    url(r'^forgot', views.forgot),



]

