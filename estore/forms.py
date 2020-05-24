from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    username = forms.CharField(required=True, 
                                min_length=4,
                                max_length=50,
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'id': 'username',
                                }))
    email = forms.EmailField(required=True,
                                widget=forms.EmailInput(attrs={
                                    'class': 'form-control',
                                    'id': 'email',
                                    'placeholder': 'example@mail.com'
                                }))
    password = forms.CharField(required=True, 
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control',
                                    'id': 'password',
                                }))
    password2 = forms.CharField(required=True, 
                                label='Password Confirmation', 
                                widget=forms.PasswordInput(attrs={
                                    'class':'form-control'
                                }))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username = username).exists():
            raise forms.ValidationError('username exists in database, please use other')

        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email = email).exists():
            raise forms.ValidationError('email exists in database, please use other')

        return email

    def clean(self):
        cleaned_data = super().clean()  #Get method clean from parent class Form
        if cleaned_data.get('password2') != cleaned_data.get('password'): #Note that password2 depends of password
            self.add_error('password2', 'Password doesnt match') #Adding error to field password2
