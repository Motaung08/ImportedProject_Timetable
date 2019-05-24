from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    url(r'^', views.courses),
    url(r'^(?P<STDN>[0-9]+)/courses', views.courses),
    url(r'^staff(?P<Staff_No>[0-9]+)/courses', views.StaffCourses),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

