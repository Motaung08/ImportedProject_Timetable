from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import HttpResponse,render, redirect
from .models import StudentsRegister, Lecturer, RegisteredStaffs
from django.conf import settings
from django.core.files.storage import FileSystemStorage


def login(request):
    context = {
        'staff': Lecturer.objects.all(),
        'students': StudentsRegister.objects.all(),

    }

    return render(request, 'Register/Log_in.html', context)


def dummy(request, STDN):

    try:
        kep = request.POST.get('uname', False)
        stdin = int(request.POST.get('uname', False))
        stdnum = stdin
        pswin = request.POST.get('psw', False)
        user = StudentsRegister.objects.get(Student_No=stdin, Password=pswin)
    except StudentsRegister.DoesNotExist:
        if(kep):
            return render(request, 'Register/Log_in.html', {'error_message': "Wrong password or Student number", })
        else:
            return render(request, 'Register/Log_in.html')
    else:

        return render(request, 'Register/Loggedin.html', {'STDN': STDN})


def staff(request,Staff_No):

    try:
        kep = request.POST.get('uname', False)
        stdin = int(request.POST.get('uname', False))
        stdnum = stdin
        pswin = request.POST.get('psw', False)
        user = Lecturer.objects.get(Lect_No=stdin, Password=pswin)
        user1 = RegisteredStaffs.objects.filter(Staff_no=Staff_No)
    except StudentsRegister.DoesNotExist:
        if(kep):
            return render(request, 'Register/Log_in.html', {'error_message': "Wrong password or Student number", })
        else:
            return render(request, 'Register/Log_in.html')

    else:

        return render(request, 'Register/lecturer_page.html', {'STDN': Staff_No,'staff': user1})


   # return render(request, 'Register/lecturer_page.html')