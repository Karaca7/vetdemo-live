



from django.forms import ModelForm

from django.contrib.auth.models import User


class UserCreate(ModelForm):
    class Meta:
        model=User
        fields=["username","password","first_name","last_name","email"]