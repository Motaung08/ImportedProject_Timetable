from django.contrib import admin
from .models import StudentsRegister, Login

admin.site.register(StudentsRegister)
admin.site.register(Login)

from .models import StudentsRegister, Login, Lecturer, Courses, Announcements, Class, RegisteredStd, RegisteredStaffs

admin.site.register(StudentsRegister)
admin.site.register(Login)
admin.site.register(Lecturer)
admin.site.register(Courses)
admin.site.register(Announcements)
admin.site.register(Class)
admin.site.register(RegisteredStd)
admin.site.register(RegisteredStaffs)

