from django.shortcuts import render

# Create your views here.
def first(request):
    return render(request,'first.html',context={'name':'sanju','age':22})


def second(request):
    return render(request,'second.html',{'name':'pavan','age':21})

