from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from users.forms import UserForm

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('usersname')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password = raw_password)
            """
            13번 user 반환값이 계속 none 반환됨
            이후 웹사이트 내에서 login에 이상 없어 우선 보류
            아니근데 어떻게 이메일이 같이 들어가는거야
            뭔데진짜
            """
            if user:
                login(request, user)
            else:
                print("user 유효하지 않음")
            return redirect('/')
    else:
        form = UserForm()
    return render(request, 'users/signup.html', {'form' : form})