from django.shortcuts import render


def logg(request):

    return render(request, 'Register/Loggedin.html')
