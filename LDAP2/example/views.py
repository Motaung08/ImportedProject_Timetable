from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from ldap3 import Server, Connection, ALL, ALL_ATTRIBUTES, NTLM



def index(request):
    server = Server('ldap://ss.wits.ac.za:389', get_info=ALL)
    #conn = Connection(server, auto_bind=True)
    conn = Connection(server, user="students\\/*student number*/", password="/*password*/", authentication='SIMPLE', auto_bind= True)

    print(conn.search('dc=ss,dc=wits,dc=ac,dc=za','(uid=/*student number*/)', attributes= ALL_ATTRIBUTES))

    print(conn.entries)



    print(" start \n")
    print(conn)
    #print(server.info)
    print("\n")
    print(conn.extend.standard.who_am_i())
    print("\n")
    print(conn.start_tls())

    print(" \n end")


    return HttpResponse("<h1> Hello World </h1>" + str(conn.entries))

