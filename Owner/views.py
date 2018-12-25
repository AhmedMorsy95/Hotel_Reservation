from django.contrib.auth import login, authenticate,logout
from django.shortcuts import render, redirect

from Owner.forms import SignUpForm
from django.http import HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect
from Reservation.models import Extend_Stay
from django.urls import  reverse

from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.views import auth_logout


def login_Page(request):
    if request.method == 'POST':
          username = request.POST['username']
          password = request.POST['password']
          user = authenticate(username=username, password=password)
          if user is not None:
                  login(request, user)
                  return redirect('http://127.0.0.1:8000/Owner/home')
          else:
              # Return an 'invalid login' error message.
              return render(request,'Owner/login.html')
    else:
        # the login is a  GET request, so just show the user the login form.
        return render(request,'Owner/login.html', {})


def logout_Page(request):
   if request.method== "POST":
     logout(request)
     return HttpResponseRedirect("/Owner/login/")


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
            return redirect('http://127.0.0.1:8000/Owner/home')
    else:
        form = SignUpForm()
    return render(request, 'Owner/signup.html', {'form': form})
def home(request):
    return render (request, 'Owner/home.html')
def direct(request):
     return redirect('http://127.0.0.1:8000/Request/addHotel')


def rdirect(request):
    return redirect('http://127.0.0.1:8000/Request/showHotels')

# def show_extension_requests(request):
#     all = Extend_Stay.objects.all()
#
#     return render(request, 'Owner/show_extension_requests.html', {'all': all})
