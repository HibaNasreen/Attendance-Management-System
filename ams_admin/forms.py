from django import forms
from accounts.models import Profile
class StaffRegisterForm(forms.Form):
    first_name = forms.CharField(label="First name", max_length=100)
    last_name = forms.CharField(label="Last name", max_length=100)
    email = forms.EmailField(label='Email')
    username = forms.CharField(label="Username")
    password = forms.CharField(widget=forms.PasswordInput())
 