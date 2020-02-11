from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from forum.forms import ThreadForm
from forum.models import Thread
from django.utils.datastructures import MultiValueDictKeyError
from django.db.models import Q


#For search
def search(query=None):
    queryset=[]
    queries = query.split(" ") #split: this will convert the strings into list
    for q in queries:
        thread = Thread.objects.filter(
        Q(title__icontains=q) |
        Q(description__icontains=q)
        )
        for t in thread:
            queryset.append(t)
    return list(set(queryset))  #typecasting: changing the type of a variable.

def home(request):
    form=ThreadForm()
    threads = Thread.objects.all()
    context={'form':form, 'threads':threads}
    query=""
    try:
        if request.GET:
            query=request.GET['searchKey']
            thread = search(str(query))
            return render(request, 'home.html', {'threads': thread})
    except MultiValueDictKeyError:
        return render(request, 'home.html', context)
    return render(request, 'home.html', context)

def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'The username is already taken!!!')
                return redirect('user:signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'The email alreay exists')
                return redirect('user:signup')
            else:
                user=User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password2)
                user.save()
                return redirect('user:login')
        else:
            messages.info(request, 'The passwords did not match!!!')
            return redirect('user:signup')
    else:
        return render(request, 'register/signup.html')

def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('user:home')
        else:
            messages.info(request, 'Please enter valid username and password!!!')
            return redirect('user:login')
    else:
        return render(request, 'register/login.html')

def logout(request):
    auth.logout(request)
    return redirect('user:home')

@login_required
def user_profile(request):
    user_id=request.user
    user=User.objects.get(pk=user_id.id)
    return render(request, 'register/user_profile.html', {'user':user})

@login_required
def update(request):
    user_info=request.user
    user=User.objects.get(pk=user_info.id)
    return render(request, 'register/update.html', {'user':user})

def update_completed(request):
    user_info=request.user
    user=User.objects.get(pk=user_info.id)
    if request.method=="POST":
        user.username=request.POST['username']
        user.first_name=request.POST['first_name']
        user.last_name=request.POST['last_name']
        user.email=request.POST['email']
        if User.objects.filter(username=user.username).exists():
            messages.info(request, 'This username is already taken!!!')
            return redirect('user:update_profile')
        elif User.objects.filter(email=user.email).exists():
            messages.info(request, 'This email is already taken!!!')
            return redirect('user:update_profile')
        else:
            user.save()
            #messages.info(request, 'Your profile has been successfully updated!!!')
            return redirect('user:login')
    else:
        return render(request, 'home.html')
