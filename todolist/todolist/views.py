from django.shortcuts import render, redirect
from .models import ListObject
# Create your views here.

def home_page(request):
    return render(request , 'todolist/HomePage.html')

def main_page(request):
    if request.method == 'POST':
        lobjecttext = request.POST.get('lobjecttext', False)
        lobject = ListObject(text = lobjecttext)
        lobject.save()
        return redirect('todolist:main_page')
    lobjects = ListObject.objects.all()
    context = {
        'lobjects': lobjects
    }
    return render(request, 'todolist/mainpage.html', context)