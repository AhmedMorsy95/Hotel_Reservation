from django.shortcuts import render
from django.shortcuts import render, redirect, HttpResponse, render_to_response, HttpResponseRedirect
from Reservation.Reserve_Form import Reserve_info
from django.contrib import messages
from django.contrib.auth.models import User
from Customer.models import customer
from django.contrib.messages import get_messages
from Reservation.models import Reservations
from Room.models import room
from django.utils import timezone
import moment
from datetime import datetime



def reserve_info(request):
    form = Reserve_info()
    if request.method == 'POST':
        form = Reserve_info(request.POST, request.FILES)
        if form.is_valid():
            check_in = form.cleaned_data['Check_in_time']
            room_ID = get_messages(request)
            check_out = form.cleaned_data['Check_out_time']
            name = User.objects.get(username=request.user.username)
            user = customer.objects.get(user_name=name)
            customer_id = customer.objects.get(pk=user.id)
            for x in room_ID:
                room_id = room.objects.get(pk=(int(str(x))))
                break
            order = Reservations()
            order.customer_id = customer_id
            order.room_id = room_id
            order.from_date = check_in
            order.to_date = check_out
            order.save()
            return redirect('home')
            # return HttpResponse(moment.date(timezone.now()).add(days=2).done())
    return render(request, 'reserve_info.html', {'form': form})
