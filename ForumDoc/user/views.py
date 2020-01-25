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

		if password1==password2:
			if User.objects.filter(username=username).exists():
				messages.info(request, 'Sorry! The username is already taken!')
				return redirect('user:signup')
			elif User.objects.filter(email=email).exists():
				messages.info(request, 'Sorry! The email is already in use!')
				return redirect('user:signup')
			else:
				user = User.objects.create_user(username=username, password=password2, email=email, first_name=first_name, last_name=last_name)
				user.save()
				print('user created')
				return redirect('user:login')
		else:
			messages.info(request, 'Sorry! The two asswords did not match!')
			return redirect('user:signup')
	else:
		return render(request, 'signup.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('user:home')
        else:
            messages.info(request, 'Please enter valid username or password.')
            return redirect('user:login')
    else:
        return render(request, 'login.html')