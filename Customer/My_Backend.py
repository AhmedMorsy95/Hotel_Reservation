from django.contrib.auth.models import User
from .models import customer

class MyBackEnd(object):
    """
     This is the custom backend to authenticate the user in the DB.
     if this authentication fais then django default authentication  will get called
     """
    def authenticate(self, userid, password=None):
        existing_user = User.objects.get(username=userid)
        if not existing_user:
            user_data = customer.objects.get(user_name=userid)