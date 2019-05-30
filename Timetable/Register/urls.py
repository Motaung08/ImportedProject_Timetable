from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    url(r'^$', views.login),

    url(r'^register', views.register),

    url(r'^reg', views.Reg),

    url(r'^logged', views.login),

    url(r'^courses', views.courses),

    url(r'^forgot', views.forgot),

    url(r'^reset-password', views.resetp),

    url(r'^(?P<STDN>[0-9]+)/announcement', views.astudent),

    # url(r'^announcement/made_announcement', views.MakeAnnouncement),

    url(r'^(?P<STDN>[0-9]+)/courses', views.courses),
    url(r'^(?P<STDN>[0-9]+)/timetable', views.timetable),

    # url(r'^reset-password/reset', views.resetp)

    # login/StudentNumber/

    url(r'^(?P<STDN>[0-9]+)', views.dummy),

    url(r'^staff(?P<Staff_No>[0-9]+)/courses', views.StaffCourses),
    url(r'^staff(?P<Staff_No>[0-9]+)/announcement', views.astaff),
    url(r'^staff(?P<Staff_No>[0-9]+)/make_announcement', views.make),
    url(r'^staff(?P<Staff_No>[0-9]+)/made_announcement', views.makeAnnouncement),


    url(r'^staff(?P<Staff_No>[0-9]+)', views.staff),

    #url(r'^staff(?P<Staff_No>[0-9]+)/courses', views.StaffCourses),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

