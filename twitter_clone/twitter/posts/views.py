from django.shortcuts import (render, get_object_or_404, redirect)
from django.views import generic
from posts.models import Post
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import (LoginRequiredMixin, UserPassesTestMixin)

# Create your views here.


class PostListView(generic.ListView):
    model = Post
    context_object_name = 'post_list'
    template_name = 'posts/post_list.html'
    order_by = ['date_posted']
    paginate_by = 5



class UserPostListView(generic.ListView):
    model = Post
    context_object_name = 'post_list'
    template_name = 'posts/user_posts.html'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User,username=self.kwargs.get('username',))
        return Post.objects.filter(author=user).order_by('-date_posted')





class PostDetailView(generic.DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin,generic.CreateView):
    model = Post
    fields = ('title', 'content',)

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,generic.UpdateView):
    model = Post
    fields = ('title', 'content')

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)


    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,generic.DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
