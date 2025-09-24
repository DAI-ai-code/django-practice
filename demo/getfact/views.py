from django.shortcuts import render

def fac(n):
    res = 1
    for i in range(n, 1, -1):
        res *= i
    else:
        return res

# Create your views here.
def getfact(request):
    return render(request,'getfact.html')

def show_fact(request):
    num = int(request.POST.get("number"))
    factt = fac(num)
    return render(request, 'getfact.html', {"result":factt})