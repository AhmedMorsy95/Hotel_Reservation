from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from Owner.forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.owner.phone = form.cleaned_data.get('phone')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('http://127.0.0.1:8000/Hotel/showHotels')
    else:
        form = SignUpForm()
    return render(request, 'Owner/signup.html', {'form': form})