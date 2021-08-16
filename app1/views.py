from django.shortcuts import render

# Create your views here.
def hello(request):
    return render(request,'app1.html',context={'name':'Amit','age':8})
