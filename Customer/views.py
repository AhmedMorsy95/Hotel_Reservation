import datetime
from django.shortcuts import render, redirect, HttpResponse, render_to_response, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from .sign_up import Register
from .models import customer
from .login import Login
from django.contrib.auth.models import User
from django.template import RequestContext
from Customer.models import customer
from Hotel.models import hotel
from Reservation.models import Reservations
from django.http import HttpResponse
from .customerForms import CustomerForm
from Room.models import room
from Customer.customerForms import forms
from Hotel.addHotelForm import HotelForm
from .searchForms import searchForm
from django.contrib import messages
from Location .models import  location
from django.utils.timezone import utc
from Room.models import room
from Reservation.models import Reservations

def index(request):

    if request.method == 'POST':
        data = CustomerForm(request.POST , request.FILES)
        if data.is_valid():
            dummy = customer()
            dummy.email = data.cleaned_data['email']
            dummy.password = data.cleaned_data['password']
            dummy.username = data.cleaned_data['username']
            dummy.mobile = data.cleaned_data['mobile']
            dummy.save()
            return HttpResponse("Added Successfully!")
        else:
            return HttpResponse("error")
    form = CustomerForm()
    name = User.objects.get(username=request.user.username)
    return render(request,'Customer/index.html',{'form' : form,'username':name})

def home(request):
    all = hotel.objects.all()
    search = searchForm()
    if request.method == 'POST':
        data = searchForm(request.POST, request.FILES)
        if data.is_valid():
            countryfield = data.cleaned_data['country']
            all = hotel.objects.filter(country = countryfield)

            cityfield = data.cleaned_data['city']
            if cityfield:
                all = all.filter(city = cityfield)

            starsfield = data.cleaned_data['stars']
            if starsfield:
                all = all.filter(stars = starsfield)
            return render(request, 'Customer/home.html', {'hotels': all})
    name = User.objects.get(username=request.user.username)
    return render(request,'Customer/home.html',{'hotels' : all, 'search' : search, 'username':name})

def reserve(request,id):
    all = hotel.objects.filter(pk=id)
    all_single_rooms = room.objects.filter(hotel_id=id , room_type='single')
    all_double_rooms = room.objects.filter(hotel_id=id, room_type='double')
    all_rooms = []
    if all_single_rooms:
        all_rooms.append(all_single_rooms[0])

    if all_double_rooms:
        all_rooms.append(all_double_rooms[0])

    name = User.objects.get(username=request.user.username)
    return render(request,'Customer/reserve.html',{'hotels' : all ,  'all_rooms':all_rooms,'username':name})


def user_login(request):
    form = Login()
    if request.method == 'POST':
        form = Login(request.POST)
        if form.is_valid():
            customers = customer()
            username = form.cleaned_data['user_name']
            password = form.cleaned_data['password']
            record = customer.objects.filter(user_name=username, password=password)
            user = authenticate(username=username, password=password)
            if  (user is not None) and (len(record)!=0):
                login(request, user)
                return redirect('home')
            else:
                return HttpResponse("Shitt")
        else:
            return HttpResponse("wrong form")
    return render(request, 'Customer/login.html', {'form':form})

def logged_in(request):
    return HttpResponseRedirect('showHotel/')

def signup(request):
    form = Register()
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            user_data = customer()
            user_data.user_name = form.cleaned_data['user_name']
            user_data.email = form.cleaned_data['email']
            user_data.mobile = form.cleaned_data['mobile']
            user_data.password = form.cleaned_data['password']
            existing_user = authenticate(email=user_data.email,password=user_data.password)
            prev_customer = customer.objects.filter(email=user_data.email, user_name=user_data.user_name)
            if  len(prev_customer)  == 0:
                user = User.objects.create_user(username=user_data.user_name, password=user_data.password, email=user_data.email)
                user.save()
                user_data.save()
                return redirect('login')
            else:
                return redirect('signup')
    return render(request, 'Customer/signup.html', {'form': form})

def reserve_room(request,room_id):
    messages.add_message(request, messages.INFO , room_id)
    return redirect('reserve_info')

1
def show_reservations(request):
    name = User.objects.get(username=request.user.username)
    cur_customer = customer.objects.filter(user_name=name.username)
    my_table = []
    hotels = []
    if cur_customer:
        cur_customer = cur_customer[0]
        now = datetime.date.today()
        my_table = Reservations.objects.filter(customer_id = cur_customer.id,confirmed=False,from_date=now)
    return  render(request,'Customer/show_reservations.html' , {'name':name, 'table':my_table} )

def confirm(request,reservation_id):
    reservation = Reservations.objects.get(pk=reservation_id)
    reservation.confirmed = True
    reservation.save()
    return redirect('show_reservations')


