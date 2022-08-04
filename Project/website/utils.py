import random
from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six
import datetime
from django.utils import timezone



class passwordgenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (six.text_type(user.pk) + six.text_type(timestamp) +  six.text_type(user.is_active))
    
TokenGenerator = passwordgenerator()

def GameExpiration():
    return timezone.now() + datetime.timedelta(minutes=10)

def RoundResult():
    num = []
    for i in range(10):
        value = num.append(random.randint(1,20))
    return value









    