from django import forms
from AppTwo.models import User

class NewUserForm(forms.ModelForm):
    #custom validations can go here
    class Meta():
        model = User
        fields = '__all__'
