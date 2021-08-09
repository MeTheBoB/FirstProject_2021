from django.shortcuts import render
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.contrib import messages
from django.urls import reverse
from django.views.generic import (DeleteView,ListView,CreateView,DetailView,RedirectView)
from django.shortcuts import get_object_or_404
from . import models
# Create your views here.

class CreatGroup(LoginRequiredMixin,CreateView):
    fields = ('name','description')
    model = models.Group

class SingleGroup(DetailView):
    model = models.Group
    template_name = 'groups/group_detail.html'

class ListGroups(ListView):
    model = models.Group

class JoinGroup(LoginRequiredMixin,RedirectView):
    def get_redirect_url(self,*args,**kwargs):
        return reverse('groups:single',kwargs={'slug':self.kwargs.get('slug')})

    def get(self,request,*args,**kwargs):
        group = get_object_or_404(Group,slug=self.kwargs.get('slug'))
        try:
            GroupMember.objects.create(user=self.request.user,group=group)
        except IntregrityError:
            messages.warning(self.request,'warning already a memeber!')
        else:
            messages.succes(self.request,'You are now a memeber!')

        return super().get(request,*args,**kwargs)


class LeaveGroup(LoginRequiredMixin,RedirectView):
    def get_redirect_url(self,*args,**kwargs):
        return reverse('group:single',kwargs={'slug':self.kwargs.get('slug')})

    def get(self,*args,**kwargs):
        try:
            memebership = models.GroupMember.objects.filter(
            user=self.request.user,
            group__slug=self.kwargs.get('slug')
            ).get()
        except models.GroupMember.DoesNotExist:
            messages.warning(self.request,'sorry your are not in the group')
        else:
            memebership.delete()
            message.succes(self.request,'Yoy have left the group!')
        return super().get(request,*args,**kwargs)
