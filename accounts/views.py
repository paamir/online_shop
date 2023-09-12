from django.shortcuts import render
from django.urls import reverse_lazy
# from django.views.generic import CreateView

from accounts.models import CustomUser
from .forms import UserCreateCustomForm

# Create your views here.


# class SignUpView(CreateView):
#     template_name = 'registration/signup.html'
#     model = CustomUser
#     form_class = UserCreateCustomForm
#     success_url = reverse_lazy('login')
