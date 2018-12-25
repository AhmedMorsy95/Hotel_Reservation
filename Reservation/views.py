from django.shortcuts import render, redirect, HttpResponse, render_to_response, HttpResponseRedirect
from Reservation.Reserve_Form import Reserve_info
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
import moment
from testing.helper_testing import fakeTime, getTimenow, refresh_db
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from Reservation.test_form import test_form
from Room.models import room
from Hotel.models import hotel
from Reservation.models import Reservations
from Customer.models import customer


def reserve_info(request):
    form = Reserve_info()
    if request.method == 'POST':
        form = Reserve_info(request.POST, request.FILES)
        if form.is_valid():
            check_in = form.cleaned_data['Check_in_time']
            room_ID = get_messages(request)
            check_out = form.cleaned_data['Check_out_time']
            name = User.objects.get(username=request.user.username)
            user = customer.objects.get(user_name=name.username)
            customer_id = customer.objects.get(pk=user.id)
            found_free = 0
            for x in room_ID:
                room_id = room.objects.get(pk=(int(str(x))))
                break
            if user.black_listed == 0:
                room_temp = room.objects.get(pk=room_id.id)
                room_group = room.objects.filter(room_type=room_temp.room_type, hotel_id=room_temp.hotel_id)
                now = moment.now().format("YYYY-M-D")
                for r in room_group:
                    room_reservations = Reservations.objects.filter(room_id=r.id)
                    all_room_res = len(room_reservations)
                    i = 0
                    for res in room_reservations:
                        if(check_in < res.from_date and check_out < res.to_date) or (check_in > res.from_date and check_out > res.to_date):
                            i+=1
                    if(i == all_room_res):
                        free_room = r
                        found_free = 1
                        break
                if(found_free == 1):
                    order = Reservations()
                    order.customer_id = customer_id
                    order.room_id = room_id.id
                    order.from_date = check_in
                    order.to_date = check_out
                    order.save()
                else:
                    # messages.add_message(request, messages.INFO, "No Rooms Available in that timing")
                    messages.add_message(request, messages.INFO, room_id.id)
                    return redirect('reserve_info')
            else:
                messages.add_message(request, messages.INFO, "User is blocked for 7 days")
                return redirect('home')
            # messages.add_message(request, messages.INFO, 'Reservation Successifully!')
            # user_reservations = Reservations.objects.filter(customer_id=customer_id.pk)
            # print(len(user_reservations))
            # if user_reservations.count() >= 5:
            #     print('passed')
            #     send_mail(
            #         'Congratulations!',
            #         'You get a discount 5%',
            #         settings.EMAIL_HOST_USER,
            #         ['aessam72@gmail.com'],
            #         fail_silently=False,
            #     )
            return redirect('home')
    return render(request, 'reserve_info.html', {'form': form})

def time_advance(request):
    form = test_form()
    if request.method == 'POST':
        form = test_form(request.POST, request.FILES)
        if form.is_valid():
            advaced_days = form.cleaned_data['advanced_days']
            fakeTime(int(advaced_days))
            return redirect('admin')
    return render(request, 'form.html', {'form':form})

def Normal(request):
    refresh_db(moment.now().format("YYYY-M-D"), 0)
    return redirect('admin')