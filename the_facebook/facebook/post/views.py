from django.shortcuts import (render, get_object_or_404, redirect)
from django.views import generic
from django.contrib.auth.mixins import (LoginRequiredMixin, UserPassesTestMixin)
from post.models import Post, Comment
from django.contrib.auth.models import User
# Create your views here.




class PostListView(LoginRequiredMixin,generic.ListView):
    model = Post
    context_object_name = 'post_list'
    template_name = 'home_index.html'
    ordering = ['-date_posted']
    paginate_by = 5




class UserPostListView(generic.ListView):
    model = Post
    context_object_name = 'post_list'
    template_name = 'post/user_post_list.html'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User,username=self.kwargs.get('username',))
        return Post.objects.filter(author=user).order_by('-date_posted')





class PostDetailView(LoginRequiredMixin,generic.DetailView):
    model = Post



class PostCreateView(LoginRequiredMixin,generic.CreateView):
    model = Post
    fields = ('title','message','image_post')

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,generic.UpdateView):
    model = Post
    fields = ('title','message','image_post')


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


class CommentCreateView(LoginRequiredMixin,generic.CreateView):
    model = Comment
    fields = ('message',)

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
