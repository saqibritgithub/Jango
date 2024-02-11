from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html', {'name': 'Saqib MOON, waqar azeem, usama haider'})

def add(request):
    # Use request.POST instead of request.post
    value1 = int(request.POST.get('num1', 0))  # Using get method to avoid KeyError
    value2 = int(request.POST.get('num2', 0))  # Using get method to avoid KeyError

    res = value1 + value2
    return render(request, "result.html", {'result': res})
