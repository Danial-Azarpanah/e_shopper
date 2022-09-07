from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django.core import validators

from .models import User


def start_with_09(value):
    """
    Custom validator for phone number
    to start with 09
    """
    if value[0:2] != "09":
        raise forms.ValidationError("Phone number should start with 09")


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='گذرواژه', widget=forms.PasswordInput)
    password2 = forms.CharField(label='تایید گذرواژه', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('phone',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('phone', 'password', 'is_active', 'is_admin')


class LoginForm(forms.Form):
    """
    The form used for logging users in
    """
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                          'placeholder': 'Your Phone'}),
                            validators=[start_with_09])
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'Your Password'}))

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if len(phone) > 11:
            raise ValidationError(
                'Your phone number is longer than 11 digits! it is %(value)s',
                'long_phone_number',
                params={"value": f"{len(phone)}"}
            )
        return phone
