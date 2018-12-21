import moment
from Reservation.models import Reservations, Blacklisted

def getTimenow():
    return moment.now().format("YYYY-M-D")

def fakeTime(days_to_add):
    date = moment.now().add(days=days_to_add).format("YYYY-M-D")
    refresh_db(date)
    return date

def refresh_db(fake_date):
    all = Reservations.objects.filter(confirmed=False)
    for i in all:
        if str(i.from_date) < fake_date:
            bad_boy = Blacklisted()
            bad_boy.from_date = i.from_date
            bad_boy.customer_id = i.customer_id
            bad_boy.save()

