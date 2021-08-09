from django.shortcuts import (render,redirect)
from account.forms import RegistrationForm
from django.contrib import messages

# Create your views here.


def Registration(request):

    if request.method == 'POST':
        user_form = RegistrationForm(data=request.POST)

        if user_form.is_valid():
            user_form.save()
            messages.success(request,f'Your account has been created')
            return redirect('account:login')
        else:
            print(user_form.errors)

    return render(request,'account/register.html',{'form':RegistrationForm()})
