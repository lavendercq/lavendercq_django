from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.urls import reverse


def index(request):
    pass

    return HttpResponse("OK!!!")


def say(request):
    pass
    return HttpResponse("say")


def sayhello(request):
    pass
    return HttpResponse("sayhello")


def weather(request, city, year):
    print("city=%s" % city)
    print("year=%s" % year)
    return HttpResponse("ok")


def qs(request):
    # url = reverse('user:say')
    a = request.GET.get("a")
    b = request.GET.get("b")
    alist = request.GET.getlist("a")
    print(a)
    print(b)
    print(alist)
    return HttpResponse('ok')


def post_body(request):
    a = request.POST.get("a")
    b = request.POST.get("b")
    alist = request.POST.getlist("a")
    print(a)
    print(b)
    print(alist)
    return HttpResponse('ok')
