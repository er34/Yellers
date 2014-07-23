from django import forms

class RegistrationForm(forms.Form):
    login = forms.CharField(max_length=100, 
                    widget=forms.TextInput(attrs={'placeholder': 'Search'}))
    email = forms.CharField(max_length=100, 
                    widget=forms.TextInput(attrs={'placeholder': 'E-mail'}))
    password = forms.CharField(label='Password', max_length=100, 
                    widget=forms.TextInput(attrs={'placeholder': 'Password'}))
    passwordagain = forms.CharField(label='Password again', max_length=100, 
                    widget=forms.TextInput(attrs={'placeholder': 'Password again'}))
    firstname = forms.CharField(label='First name', max_length=100, 
                    widget=forms.TextInput(attrs={'placeholder': 'First name'}))
    lastname = forms.CharField(label='Last name', max_length=100, 
                    widget=forms.TextInput(attrs={'placeholder': 'Last name'}))