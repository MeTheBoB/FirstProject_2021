from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm



class RegistrationForm(UserCreationForm):
    # name = forms.CharField(required=True)
    surname = forms.CharField(required=False)
    age = forms.IntegerField(required=True)
    email = forms.EmailField()
    # password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = ('username','surname','age','email','password1')


    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label = 'Name'


    def clean(self):
        all_clean_data = super().clean()
        age = all_clean_data['age']

        if age < 13:
            raise forms.ValidationError('You need be 13 years old to be able to use facebook!')
