from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class SignupForm(UserCreationForm):
    username = forms.CharField(label=False)
    email = forms.EmailField(label=False)
    password1 = forms.CharField(widget=forms.PasswordInput(), label=False)
    password2 = forms.CharField(widget=forms.PasswordInput(), label=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

   
    helper = FormHelper()
    helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
    helper.form_method = 'POST'


    