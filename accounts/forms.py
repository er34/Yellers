from django import forms
from captcha.fields import CaptchaField
from django.contrib.admin.widgets import AdminDateWidget 

class RegistrationForm(forms.Form):
    login = forms.CharField(max_length=30, 
                    widget=forms.TextInput(attrs={'placeholder': 'Login'}))
    email = forms.EmailField(max_length=50, 
                    widget=forms.TextInput(attrs={'placeholder': 'E-mail'}))
    password = forms.CharField(label='Password', max_length=30, 
                    widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    passwordagain = forms.CharField(label='Password again', max_length=30, 
                    widget=forms.PasswordInput(attrs={'placeholder': 'Password again'}))
    firstname = forms.CharField(label='First name', max_length=30, 
                    widget=forms.TextInput(attrs={'placeholder': 'First name'}))
    lastname = forms.CharField(label='Last name', max_length=30, 
                    widget=forms.TextInput(attrs={'placeholder': 'Last name'}))
    captcha = CaptchaField()
    
class LoginForm(forms.Form):
    login = forms.CharField(max_length=30, 
                    widget=forms.TextInput(attrs={'placeholder': 'Login'}))
    password = forms.CharField(label='Password', max_length=30, 
                    widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

class AccountForm(forms.Form):
    login = forms.CharField(max_length=30, 
                    widget=forms.TextInput(attrs={'placeholder': 'Login'}))
    email = forms.EmailField(max_length=50, 
                    widget=forms.TextInput(attrs={'placeholder': 'E-mail'}))
    password = forms.CharField(label='Password', max_length=30, 
                    widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    passwordagain = forms.CharField(label='Password again', max_length=30, 
                    widget=forms.PasswordInput(attrs={'placeholder': 'Password again'})) 
    firstname = forms.CharField(label='First name', max_length=30, 
                    widget=forms.TextInput(attrs={'placeholder': 'First name'}))
    lastname = forms.CharField(label='Last name', max_length=30, 
                    widget=forms.TextInput(attrs={'placeholder': 'Last name'}))
    middle_name =forms.CharField(max_length=30, 
                    widget=forms.TextInput(attrs={'placeholder': 'Middle name'}))
    avatar = forms.ImageField(label= 'User picture')
    phone = forms.CharField(max_length=30, 
                    widget=forms.TextInput(attrs={'placeholder': 'Phone'}))
    married = forms.BooleanField(label= 'Married')
    birthday = forms.DateField(widget = AdminDateWidget)
    organisation = forms.CharField(label='Last name', max_length=30, 
                    widget=forms.TextInput(attrs={'placeholder': 'Organization'}))
    politic = forms.CharField(label='Last name', max_length=30, 
                    widget=forms.TextInput(attrs={'placeholder': 'Politic'}))
    religion = forms.CharField(label='Last name', max_length=30, 
                    widget=forms.TextInput(attrs={'placeholder': 'Religion'}))
    addr_index = forms.CharField(label='Last name', max_length=30, 
                    widget=forms.TextInput(attrs={'placeholder': 'Zip code'}))
    addr_country = forms.CharField(label='Last name', max_length=30, 
                    widget=forms.TextInput(attrs={'placeholder': 'Country'}))
    addr_region = forms.CharField(label='Last name', max_length=30, 
                    widget=forms.TextInput(attrs={'placeholder': 'Region'}))
    addr_area = forms.CharField(label='Last name', max_length=30, 
                    widget=forms.TextInput(attrs={'placeholder': 'Area'}))
    addr_city = forms.CharField(label='Last name', max_length=30, 
                    widget=forms.TextInput(attrs={'placeholder': 'City'}))
    addr_home = forms.CharField(label='Last name', max_length=30, 
                    widget=forms.TextInput(attrs={'placeholder': 'home'}))
    addr_MO = forms.CharField(label='Last name', max_length=30, 
                    widget=forms.TextInput(attrs={'placeholder': 'MO'}))
    gps =  forms.CharField(label='Last name', max_length=30, 
                    widget=forms.TextInput(attrs={'placeholder': 'Gps coordinates'}))