from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from django.views.generic import (DeleteView,ListView,CreateView,DetailView)
from django.http import Http404

from braces.views import SelectRelatedMixin

from . import models
from . import forms

from django.contrib.auth import get_user_model
User = get_user_model

class PostList(SelectRelatedMixin,ListView):
    models = models.Post
    select_related = ('user','group')



class UserPosts(ListView):
    model = models.Post
    template_template = 'posts/user_post_list.html'


    # def get_queryset(self):
    #     try:
    #         self.post.user = User.objects.prefetch_related('posts').get(username__iexact=self.kwargs.get('username'))
    #     except:
    #         raise Http404
    #     else:
    #         return self.post_user.post.all()
    #
    # def get_context_data(self,**kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['post_user'] = self.post_user
    #     return context



class PostDetail(SelectRelatedMixin,DetailView):
    model = models.Post
    select_related = ('user','group')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__username__iexact=self.kwargs.get('username'))


class CreatePost(LoginRequiredMixin,SelectRelatedMixin,CreateView):

    fields = ('message','group')
    model = models.Post

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        sef.object.user
        return super().form_valid(form)



class DeletePost(LoginRequiredMixin,SelectRelatedMixin,DeleteView):
    model = models.Post
    select_related = ('user','group')
    success_url = reverse_lazy('post:all')

    def get_queryset(Self):
        queryset=super().get_queryset()
        return queryset.filter(user_id = self.request.user.id)

    def delete(self,*args,**kwargs):
        messages.succes(self.request,'Post Deleted')
        return super().delete(*args,**kwargs)
