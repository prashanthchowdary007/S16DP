from django.shortcuts import render, redirect


# Create your views here.

# Template Rending
def sample3(request):
    return render(request, 'index.html')


# contest passing
def sample4(request, name):
    return render(request, 'index2.html', {'name': name})


# contest passing
def sample5(request):
    name = "good Evening"
    return render(request, 'index2.html', {'name': name})


def sample6(request):
    lst = ['ABC', 'DEF', 'GHI']
    return render(request, 'lst.html', {'lst': lst})


# Redirect
def sample7(request):
    return redirect('TR')


# Template inheritance
def sample8(request):
    return render(request, 'base.html')


# static content
def sample9(request):
    return render(request, 'index4.html')
