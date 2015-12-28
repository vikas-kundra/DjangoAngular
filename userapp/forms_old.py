from django import forms

from .models import User
from .models import User_new
from django.http import HttpResponseRedirect

# We need to tell Django that this form is Model Form so that it will do some magic for us !!!
class PostForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        password_first = self.cleaned_data.get('password')
        password_second = self.cleaned_data.get('confirm_password')

        if password_first and password_first != password_second:
            raise forms.ValidationError("Passwords don't match!!! Enter Correct password")

        return self.cleaned_data

    class Meta:
        #model = User
        model = User_new
        widgets = {
        'password': forms.PasswordInput(),
    }
        fields = ('user_name','country','age','password')




class LoginForm(forms.ModelForm):

    #logged_in_status = forms.CharField(widget= forms.HiddenInput())
    #def clean(self):
    #    user_name_entered = self.cleaned_data.get('user_name')
    #    password_entered = self.cleaned_data.get('password')
    #    password_list = User_new.objects.filter(user_name__iexact=user_name_entered, password = password_entered)
    #    if len(password_list) == 0:
    #        raise forms.ValidationError("Entered password doesn't match")

    #next = forms.CharField(widget=forms.HiddenInput())
    #    return self.cleaned_data
    class Meta:
        model = User_new
        widgets = {
        'password': forms.PasswordInput(),
    }
        fields = ('user_name','password')