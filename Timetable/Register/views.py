from django.shortcuts import render, get_object_or_404
import sys


from django.shortcuts import HttpResponse,render, redirect
from .models import StudentsRegister,Login



def login(request):

    try:
        kep = request.POST.get('uname', False)
        stdin = int(request.POST.get('uname', False))
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




def logged(request):



    return render(request, 'Register/Loggedin.html')



