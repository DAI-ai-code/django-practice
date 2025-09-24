from django.shortcuts import render

# Create your views here.

def fac(n):
    res = 1
    for i in range(n, 1, -1):
        res *= i
    else:
        return res

def login(request):

    return render(request, 'fact.html')

def fact(request):
    n = request.POST.get("number")
    result = fac(int(n))

    return render(request, 'fact.html', {"result":result})
