from django import forms
from dashapp.models import Team, Members
from django.contrib.auth.models import User

class TeamForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Team
        fields = ['team_name','team_project','bio']

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email', 'password']

class MemberForm(forms.ModelForm):

    class Meta:
        model = Members
        fields = ['fName','lName']
