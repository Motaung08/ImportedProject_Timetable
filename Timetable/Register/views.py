from django.shortcuts import render, get_object_or_404
import sys

from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import HttpResponse,render, redirect
from .models import StudentsRegister, Login, Lecturer, Courses, Announcements, Class, RegisteredStd, RegisteredStaffs

stdnum = 0;

def astaff(request, Staff_No):
    print("inside function")


    user = RegisteredStaffs.objects.filter(Staff_no=Staff_No)
    #announcement = Announcements.objects.all()
    #announcement = Announcements.objects.filter(Lect_No=Staff_No)
    announcement = Announcements.objects.all().order_by('-Created')


    print(user)
    context = {
        'user': user,
        'STDN': Staff_No,
        'announcement': announcement,
    }
    print("inside function")

    return render(request, 'Register/View_announcement.html', context)

def astudent(request, STDN):
    print("inside function")


    user = RegisteredStd.objects.filter(Std_no=STDN)
    announcement = Announcements.objects.all().order_by('-Created')


    print("below s")
    context = {
        'user': user,
        'STDN': STDN,
        'announcement': announcement,
    }
    print("inside function")

    return render(request, 'Register/View_announcement.html', context)

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


    #return render(request, 'Register/dummy.html', {'STDN': STDN})




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


def make(request,Staff_No):
    print(Staff_No)
    user = RegisteredStaffs.objects.filter(Staff_no=Staff_No)

    print(user)
    context = {
        'user': user,
        'STDN': Staff_No,

    }
    return render(request, 'Register/Make_Announcement.html',context)

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


def makeAnnouncement(request, Staff_No):

    Subject = request.POST['Title']
    Course_Code = request.POST.get('Course Code')

    Content = request.POST['message']



    print(Staff_No)


    a = Announcements()
    q = Courses.objects.get(Course_Code=Course_Code[-8:])
    a.Course_Code = q

    p = Lecturer.objects.get(Lect_No=Staff_No)
    a.Lect_No = p

    a.Title = Subject
    a.Content = Content

    a.save()

    print("Done")
    return render(request, 'Register/Announcement.html')


def courses(request, STDN):
    print("inside function")


    user = RegisteredStd.objects.filter(Std_no=STDN)

    print("below s")
    context = {
        'user': user,
        'STDN': STDN,
    }
    print("inside function")

    return render(request, 'Register/Courses.html', context)

def StaffCourses(request, Staff_No):
    print("inside function")


    user = RegisteredStaffs.objects.filter(Staff_no=Staff_No)

    print("below s")
    context = {
        'user': user,
        'STDN': Staff_No,
    }
    print("inside function")

    #return HttpResponse("<h1> Hello</h1>")
    return render(request, 'Register/Courses.html', context)


def announcement(request, STDN):
    print("inside function")
    # print(stdnum);

    user = Announcements.objects.filter(id=RegisteredStd.objects.filter(Std_no=STDN).count() - 1)
    # a = Lecturer.objects.filter(Lect_No =user.)

    print("below s")
    context = {
        'user': user,
        'STDN': STDN,
    }
    print("inside function")

    return render(request, 'Register/Announcement.html', context)


def reset(request):
    print("inside reset")
    try:
        psw = request.POST['newpsw']
        stdin = int(request.POST.get('uname'))
        email = request.POST.get('emailadd')
        user = StudentsRegister.objects.get(Student_No=stdin, Email=email)
        user.Password = psw
        user.save()
        print("Helllo World")

    except StudentsRegister.DoesNotExist:
        user = None
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

        send_mail(subject, message, from_email, to_list, fail_silently=True)
        return render(request, 'Register/Log_in.html')

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

