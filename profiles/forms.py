from django.forms import ModelForm
from profiles.models import Profile


class AvatarForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('avatar',)

