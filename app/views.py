from django.shortcuts import render

# Create your views here.
def staticfile1(request):
    return render(request,'staticfile1.html')