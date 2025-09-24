from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def mypage(request):
    return HttpResponse("Hello world from django")

def bye(request):
    return HttpResponse('Bye..bye..bye')

def fact(n):
    i = 1
    for j in range(n,1,-1):
        i *= j
    return i

def home(request):
    n = request.POST.get("number")
    ans = fact(int(n))
    return HttpResponse(ans)