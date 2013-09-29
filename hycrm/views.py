# Create your views here.
from django.http.response import HttpResponse
from django.contrib.auth import authenticate,login
from django.shortcuts import render_to_response


def index(request):
    return render_to_response('login.html')

def login_view(request):
    user = authenticate(username=request.POST['username'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        print request.user
        return denglu(request)
    else:
        return weidenglu(request)

def denglu(request):
    return  HttpResponse("denglule")

def weidenglu(request):
    return HttpResponse("weidenglu")