from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class UserCreateCustomForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['email', 'username']


class UserChangeCustomForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['email', 'username']


