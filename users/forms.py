from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        pass

class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields = UserCreationForm.Meta.fields + ("email", )
        
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        del self.fields['password2']
        self.fields['email'].widget.attrs['required'] = 'required'
        self.fields['password1'].help_text = None
        self.fields['username'].help_text = None