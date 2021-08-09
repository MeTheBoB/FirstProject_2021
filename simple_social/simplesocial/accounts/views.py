from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from . import forms
from django.contrib.auth import logout
# Create your views here.

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    # After loging in will reverse to login
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
