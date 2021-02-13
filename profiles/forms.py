from django.forms import ModelForm
from .models import Profile
from django.contrib.auth import get_user_model

class AvatarForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('avatar',)

