from django.shortcuts import render, redirect
from django.urls import reverse
from account.forms import RegistrationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


def register(request):

    if request.method == 'POST':
        userform = RegistrationForm(data = request.POST)

        if userform.is_valid():
            userform.save()
            # username = userform.clean_data.get('username')
            messages.success(request,f'Your account has been created!')
            return redirect('account:login')

        else:
            print(userform.errors)
    # else:
    #     user_form = RegistrationForm()

    return render(request,'account/signup.html',{'user_form':RegistrationForm()})
