from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from users.forms import UserForm

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save() # user 정보 저장
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password) # 로그인 전 객체 생성
            login(request, user)
            messages.error("환영합니다,",username,"님!")
            return redirect('/')
    else:
        form = UserForm()
    return render(request, 'users/signup.html', {'form' : form})
def profile(request):
    return render(request, 'users/user_profile.html')