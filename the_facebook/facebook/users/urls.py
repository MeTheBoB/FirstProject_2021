from users import views
from django.urls import path, include



app_name = 'users'

urlpatterns = [
    path('profile',views.ProfileView.as_view(),name='profile'),
    path('profile-update',views.update_profile,name='update_profile')




]
