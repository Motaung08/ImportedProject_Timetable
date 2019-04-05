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

    url(r'^(?P<STDN>[0-9]+)/announcement', views.announcement),

    # url(r'^announcement/made_announcement', views.MakeAnnouncement),

    url(r'^(?P<STDN>[0-9]+)/courses', views.courses),

    # url(r'^reset-password/reset', views.resetp)

    # login/StudentNumber/

    url(r'^(?P<STDN>[0-9]+)', views.dummy),

    url(r'^staff(?P<Staff_No>[0-9]+)/courses', views.StaffCourses),

    url(r'^staff(?P<Staff_No>[0-9]+)', views.staff),

    #url(r'^staff(?P<Staff_No>[0-9]+)/courses', views.StaffCourses),

]

