from django.urls import path
from posts import views

app_name = 'posts'

urlpatterns = [
    path('posts-detail/<int:pk>/',views.PostDetailView.as_view(),name='post_detail'),
    path('user/<str:username>',views.UserPostListView.as_view(),name='user_post'),
    path('post/new/',views.PostCreateView.as_view(),name='post_create'),
    path('post/<int:pk>/update/',views.PostUpdateView.as_view(),name='post_update'),
    path('post/<int:pk>/delete/',views.PostDeleteView.as_view(),name='post_delete'),


]
