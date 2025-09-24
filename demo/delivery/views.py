from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def delivery_update(request):
    return render(request,'delivery.html')