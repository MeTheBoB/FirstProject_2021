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
        u_form = UserUpdateForm(request.POST,instance = request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance = request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Your account has been updated!')
            return redirect('users:profile')

    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)

    context ={

        'u_form': u_form,
        'p_form': p_form
    }

    return render(request,'users/update_profile.html',context)
