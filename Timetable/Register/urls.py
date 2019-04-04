from django.conf.urls import url
from . import views




urlpatterns = [

    url(r'^$', views.login),

    url(r'^register', views.register),

    url(r'^reg', views.Reg),

    url(r'^logged', views.login),

    url(r'^courses', views.courses),

    url(r'^forgot', views.forgot),

    url(r'^reset-password', views.resetp),

    url(r'^announcement', views.announcement)
]

