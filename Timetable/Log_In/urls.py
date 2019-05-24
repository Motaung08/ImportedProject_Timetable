from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include,url

urlpatterns = [

    url(r'^$', views.login),

    url(r'^logged', views.login),

    url(r'^staff(?P<Staff_No>[0-9]+)/courses', include('Courses.url')),
    url(r'^(?P<STDN>[0-9]+)/courses', include('Courses.urls')),
    url(r'^(?P<STDN>[0-9]+)/announcement',  include('Announcements.urls')),
    url(r'^staff(?P<Staff_No>[0-9]+)/announcement',include('Announcements.url')),

    url(r'^staff(?P<Staff_No>[0-9]+)/announcement', include('Announcements.url')),

    url(r'^staff(?P<Staff_No>[0-9]+)/make_announcement', include('Make_Announcements.url')),
    url(r'^staff(?P<Staff_No>[0-9]+)/made_announcement', include('Make_Announcements.urls')),


    # login/StudentNumber/

    url(r'^(?P<STDN>[0-9]+)', views.dummy),

    url(r'^staff(?P<Staff_No>[0-9]+)', views.staff),






]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

