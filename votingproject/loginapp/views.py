from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# Create your views here.
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('voteapp:voting')
            else:
                return render(request, 'loginapp/voter_login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'loginapp/voter_login.html', {'error_message': 'Invalid login'})
    return render(request, 'loginapp/voter_login.html')