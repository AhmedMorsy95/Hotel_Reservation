import moment
from Reservation.models import Reservations, Blacklisted
from Customer.models import customer

def getTimenow():
    return moment.now().format("YYYY-M-D")

def fakeTime(days_to_add):
    date = moment.now().add(days=days_to_add).format("YYYY-M-D")
    refresh_db(date, 1)
    return date

def refresh_db(fake_date, fake):
    unconfirmed_reservations = Reservations.objects.filter(confirmed=False)
    blacklisted_customers = Blacklisted.objects.all()
    if fake:
        for i in unconfirmed_reservations:
            referred_customer = customer.objects.get(id=i.customer_id.pk)
            check_in = moment.date(i.from_date).add(days=7).format("YYYY-M-D")
            print(check_in)
            print(fake_date)
            if str(i.from_date) < fake_date and referred_customer.black_listed == 0 and i.confirmed == 0 and check_in > fake_date:
                print('hi')
                bad_boy = Blacklisted()
                bad_boy.from_date = i.from_date
                bad_boy.customer_id = i.customer_id
                referred_customer.black_listed = 1
                referred_customer.save()
                bad_boy.save()
    elif fake == 0:
        for i in blacklisted_customers:
            referred_customer = customer.objects.get(id=i.customer_id.pk)
            blacklisted_date = moment.date(i.from_date).add(days=7).format("YYYY-M-D")
            if str(i.from_date) > moment.now().format("YYYY-M-D") or blacklisted_date <= fake_date:
                referred_customer.black_listed = 0
                referred_customer.save()
                i.delete()
