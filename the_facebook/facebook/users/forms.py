from django import forms
from users import models
from django.contrib.auth.models import User


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username','email')

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label = 'Name'
        self.fields['email'].label = 'E-mail'




class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = models.Profile
        fields = ('image','cover_image','biography')

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['image'].label = 'Profile picture'
