from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserUpdateForm, ProfileUpdateForm
# Create your views here.


class ProfileView(LoginRequiredMixin,generic.TemplateView):
    template_name = 'users/user_profile.html'

# @login_required
# def profile(request):
#     return render(request,'users/user_profile.html')


@login_required
def update_profile(request):
    if request.method == 'POST':
        form_user = UserUpdateForm(request.POST,instance = request.user)
        form_profile = ProfileUpdateForm(request.POST,request.FILES, instance = request.user.profile)

        if form_profile.is_valid() and form_user.is_valid():
            form_user.save()
            form_profile.save()
            messages.success(request,f'Your account has been updated!')
            return redirect('users:profile')

    else:
        form_user = UserUpdateForm(instance = request.user)
        form_profile = ProfileUpdateForm(instance = request.user.profile)

    context ={

        'form_user': form_user,
        'form_profile': form_profile
    }

    return render(request,'users/update_profile.html',context)
