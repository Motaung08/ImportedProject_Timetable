from django.shortcuts import render, get_object_or_404
import sys

from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import HttpResponse,render, redirect
from .models import StudentsRegister, Login, Lecturer, Courses, Announcements, Class, RegisteredStd, RegisteredStaffs

stdnum = 0;


def login(request):

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
        return render(request, 'Register/Loggedin.html')
        # login(request)



def loginconfirm(request):
    all_students = StudentsRegister.objects.all()
    stdin = int(request.POST.get('uname', False))
    pswin = request.POST.get('psw', False)
    try :
        user = StudentsRegister.objects.get(Student_No=stdin, Password = pswin)
    except StudentsRegister.DoesNotExist:
        user = None
    if user:
        return render(request, 'Register/Loggedin.html')
    else:
        return render(request, 'Register/Log_in.html')
        #login(request)



def forgot(request):

    return render(request, 'Register/forgot.html')


def register(request):

    return render(request, 'Register/register.html')

def resetp(request):
    return render(request, 'Register/reset.html')
    # try:
    #     kep = request.POST.get('uname', False)
    #     stdin = int(request.POST.get('uname', False))
    #     pswin = request.POST.get('psw', False)
    #     user = StudentsRegister.objects.get(Student_No=stdin, Password=pswin)
    # except StudentsRegister.DoesNotExist:
    #     if (kep):
    #         return render(request, 'Register/Log_in.html', {'error_message': "Wrong password or Student number", })
    #     else:
    #         return render(request, 'Register/Log_in.html')
    #
    # else:
    #     return render(request, 'Register/Loggedin.html')


def Reg(request):

    std = request.POST['stdnum']
    na = request.POST['na']
    email = request.POST['email']
    cellnum = request.POST['cellnum']
    psw = request.POST['psw']
    cpsw = request.POST['psw-confirm']



    a = StudentsRegister()
    a.Student_No = int(std)
    a.Name= na
    a.Email= email
    a.Password= psw
    a.CellPhone_No = int(cellnum)
    a.save()

    print(" sent Reg"),
    print(" sent Reg"),
    print(" sent Reg"),
    print(" sent Reg"),
    print(" sent Reg"),
    print(" sent Reg"),

    return render(request, 'Register/Log_in.html')

def courses(request):
    print("inside function")
    #print(stdnum);
    s = int(request.POST.get('uname', False))
    print(s)

    user = RegisteredStd.objects.filter(Std_no=1643694)

    print(user.Course_Code)
    print("below s")
    context = {
        'user': user,
    }
    print("inside function")

    return render(request, 'Register/Courses.html', context)


def reset(request):
    print("inside reset")
    try:
        psw = request.POST['newpsw']
        stdin = int(request.POST.get('uname'))
        email = request.POST.get('emailadd')
        user= StudentsRegister.objects.get(Student_No=stdin, Email=email)
        user.Password = psw
        user.save()
        print("Helllo World")

    except StudentsRegister.DoesNotExist:
        user =None
    if user:
        return render(request, 'Register/congrats.html')
    else:
        return render(request, 'Register/reset.html', {'error_message': "Wrong email or Student number"})

        return render(request, 'Register/congrats.html')


    


def logged(request):



    return render(request, 'Register/Loggedin.html')


def forgotpassword(request):
    try:

        stdin = int(request.POST.get('uname', False))
        email = request.POST.get('emailadd', False)
        user = StudentsRegister.objects.get(Student_No=stdin, Email=email)
    except StudentsRegister.DoesNotExist:
        if (stdin):
            return render(request, 'Register/forgot.html', {'error_message': "Wrong password or Student number", })
        else:
            return render(request, 'Register/fotgot.html')

    else:
        subject = 'Reset your password'
        message = 'Your password is  '
        from_email = 'tlaphane@gmail.com'
        to_list = ['tlaphane@gmail.com']

        send_mail(subject,message,from_email,to_list,fail_silently=True)
        return render(request, 'Register/Log_in.html')



