from django.contrib import admin
from .models import StudentsRegister, Lecturer,RegisteredStaffs,RegisteredStd

admin.site.register(StudentsRegister)
admin.site.register(Lecturer)
admin.site.register(RegisteredStaffs)
admin.site.register(RegisteredStd)
