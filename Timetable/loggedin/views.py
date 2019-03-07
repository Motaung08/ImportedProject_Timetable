from django.shortcuts import render


def logg(request):

    return render(request, 'loggedin/Loggedin.html')
