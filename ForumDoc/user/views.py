from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def home(request):
    count = User.objects.count()
    return render(request, 'home.html', {
        'count': count
        })



def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username = username).exists():
                messages.info(request, 'This username is already taken.')
                return redirect('user:signup')
            elif User.objects.filter(email = email).exists():
                messages.info(request, 'This email has already been taken.')
                return redirect('user:signup')
            else :
                user = User.objects.create_user(username = username, first_name = first_name, last_name = last_name, email = email, password = password2)
                user.save()
                print('Congratulation a new user has been created.')
                return redirect('user:login')

        else:
            messages.info(request, 'Please enter the correct password.')
            return redirect('user:signup')
        
    
    else:
        return render(request, 'signup.html')
    
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request, user)
            return redirect('user:home') 
        else:
            messages.info(request, 'User invalid.')
            return redirect('user:login')
    else:
        return render(request, 'login.html')
        