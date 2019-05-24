from django.contrib import admin
from .models import StudentsRegister, Lecturer,RegisteredStaffs,RegisteredStd, once

admin.site.register(StudentsRegister)
admin.site.register(Lecturer)
admin.site.register(RegisteredStaffs)
admin.site.register(RegisteredStd)
admin.site.register(once)

