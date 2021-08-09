from django.urls import path
from post.views import (PostListView,UserPostListView ,PostDetailView,
                        PostCreateView, PostUpdateView,
                        PostDeleteView,
                        CommentCreateView)



app_name = 'post'


urlpatterns = [
    path('post-list/',PostListView.as_view(),name='post_list'),
    path('user/<str:username>/',UserPostListView.as_view(),name='user_post_list'),
    path('post-detail/<int:pk>/',PostDetailView.as_view(),name='post_detail'),
    path('post-create/',PostCreateView.as_view(),name='post_create'),
    path('post/<int:pk>/update',PostUpdateView.as_view(),name='post_update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post_delete'),

    path('comment-create/',CommentCreateView.as_view(),name='comment_create')

]
