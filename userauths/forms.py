from django import forms
from userauths.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class EditProfileForm(forms.ModelForm):
    image = forms.ImageField(required=True)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'calss':'input','placeholder':'First_Name'}),required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'calss':'input','placeholder':'Last_Name'}),required=True)
    location = forms.CharField(widget=forms.TextInput(attrs={'calss':'input','placeholder':'Location'}),required=True)
    #url = forms.CharField(widget=forms.TextInput(attrs={'calss':'input','placeholder':'URL'}),required=True)
    bio = forms.CharField(widget=forms.TextInput(attrs={'calss':'input','placeholder':'BIO'}),required=True)
    class Meta :
        model =Profile
        fields=['image','first_name','last_name','location','url','bio']
        

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'prompt srch_explore'}), max_length=50, required=True)
    # username = forms.EmailInput(widget=forms.TextInput(attrs={'placeholder': 'Username'}), max_length=50, required=True)

    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'prompt srch_explore'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password', 'class': 'prompt srch_explore'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'prompt srch_explore'}))
    # email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

