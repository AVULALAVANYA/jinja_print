from django.shortcuts import render

# Create your views here.
def jinjaprint(request):
    d={'name':'Lavu','age':24}
    return render(request,'jinjaprint.html',context=d)
