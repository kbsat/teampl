from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate as auth_authenticate
from .models import User
from .forms import CreateUser


def mypage(request):

    if request.user.is_authenticated:
        user = request.user
    else:
        return redirect('index')

    return render(request, "mypage.html", {'user': user})


def logout(request):
    auth_logout(request)
    return redirect('index')


def login(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # 1. 암호화된 인증
        user = auth_authenticate(
            request, username=username, password=password)
        if user is not None:
            print(user)
            auth_login(request, user)
            return redirect('index')

        # 2. 암호화되지않은 인증
        try:
            user2 = User.objects.get(username=username, password=password)

        except:
            return render(request, 'login.html', {'error': 'ID나 비밀번호가 틀렸습니다.'})

        print("user2login"+str(user2))
        auth_login(request, user2)
        return redirect('index')
    return render(request, "login.html")


def signup(request):
    error = ''
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        signup_form = CreateUser(request.POST)
        if signup_form.is_valid():
            user = signup_form.save(commit=False)
            user.save()
            auth_login(request, user)
            return redirect('index')
        else:
            error = '아이디가 중복되었거나 형식이 틀렸습니다.'

    else:
        signup_form = CreateUser()

    return render(request, 'signup.html', {'form': signup_form, 'error': error})
