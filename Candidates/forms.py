from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from authentication.models import CustomUser
from .models import *

class CandidateCreationForm(UserCreationForm):
    post = forms.ModelChoiceField(queryset=Posts.objects.all(), required=True)
    manifesto = forms.CharField(widget=forms.Textarea, required=False)
    background_info = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = CustomUser  # Assuming CustomUser is your user model
        fields = ['id_no', 'gender', 'email','first_name','last_name', 'password1', 'password2', 'post', 'manifesto', 'background_info']

class CandidateUpdateForm(UserChangeForm):
    post = forms.ModelChoiceField(queryset=Posts.objects.all(), required=True)
    manifesto = forms.CharField(widget=forms.Textarea, required=False)
    background_info = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = CustomUser  # Assuming CustomUser is your user model
        fields = ['id_no', 'gender', 'email','first_name','last_name', 'password', 'post', 'manifesto', 'background_info']
