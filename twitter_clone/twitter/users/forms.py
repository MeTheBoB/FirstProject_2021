from django.contrib.auth.models import User
from users import models
from django import forms





class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username','email')

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label='Display name'
        self.fields['email'].label='E-mail'


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = models.Profile
        fields = ('image','biography')

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['image'].label = 'Profile picture'
