from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import HttpResponse,render, redirect
from .models import StudentsRegister, Lecturer, RegisteredStaffs, once, RegisteredStd
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from ldap3 import Server, Connection, ALL, ALL_ATTRIBUTES, NTLM




def login(request):

    return render(request, 'Register/Log_in.html')


def dummy(request, STDN):

    stdin = int(request.POST.get('uname', False))
    pswin = request.POST.get('psw', False)
    server = Server('ldap://ss.wits.ac.za:389', get_info=ALL)
    conn_stdin = "students\\"+str(stdin)
    try:
        conn = Connection(server, user=conn_stdin, password=pswin, authentication='SIMPLE',
                              auto_bind=True)
        access = "granted"
        print(access)


        #return render(request, 'Register/Loggedin.html', {'STDN': STDN})




    except:
        access = "denied"
        print(access)
        #return render(request, 'Register/Log_in.html', {'error_message': "Wrong password or Student number", })

    if(access=="granted"):
        print("returned granted")
        a = '(uid='+str(stdin)+')'
        print(conn.search('dc=ss,dc=wits,dc=ac,dc=za', a, attributes=ALL_ATTRIBUTES))

        user1 = once.objects.filter(Std_no=stdin).exists()
        if (user1 == False):
            user = once(Std_no=stdin)
            user.save()

            arr = conn.entries[0].memberOf

            for i in range(0, len(arr)):
                # print(arr[i])
                x = arr[i].split(',')
                course = x[0]
                if (len(course) == 11):
                    course_code = course[-8:]
                    print(course_code)
                    if (course_code[:-4] == "COMS"):
                        print(course_code)
                        u = RegisteredStd(Std_no=stdin, Course_Code=course_code)
                        u.save()

        return render(request, 'Register/Loggedin.html', {'STDN': STDN})

    else:
        print("returned denied")
        return render(request, 'Register/Log_in.html', {'error_message': "Wrong password or Student number", })



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