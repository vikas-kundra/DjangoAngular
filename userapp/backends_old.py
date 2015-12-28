from .models import User_new

class ClientAuthBackend(object):

    def authenticate(self, user_name=None, password=None):
        user = User_new.objects.filter(user_name__iexact=user_name, password=password)
        if len(user) == 0:
            return  None
        else:
            return user


    def get_user(self, user_id):
        try:
            return User_new.objects.get(pk=user_id)
        except User_new.DoesNotExist:
            return None