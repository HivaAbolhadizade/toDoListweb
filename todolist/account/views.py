from django.shortcuts import render, Http404, redirect
from .models import User
from django.contrib import messages
# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        if 'signup' in request.POST:
            email = request.POST.get('email', False)
            password = request.POST.get('pswd', False)
            password2 = request.POST.get('pswd2', False)
            if password != password2:
                return redirect('account:signup')
            if User.objects.filter(email=email).exists():
                return redirect('account:signup')
            new_user = User(email=email, password=password)
            new_user.save()
            return redirect ('todolist:main_page')
        elif 'login' in request.POST:
            email = request.POST.get('email')
            password = request.POST.get('pswd')
            if not User.objects.filter(email=email, password=password).exists():
                return Http404
            return redirect ('todolist:main_page')
        print('im dead')
    return render(request, 'account/SIgnUPIn.html')





   
    
    
    
