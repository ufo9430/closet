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
            user = authenticate(username=username, password=raw_password)
            print(user)
            if user:
                login(request, user)
            else:
                print("login 유효하지 않음")
            return redirect('/')
    else:
        form = UserForm()
    return render(request, 'users/signup.html', {'form' : form})