from django import forms
from .models import Group

class GroupForm(forms.ModelForm):
    codename = forms.CharField(widget=forms.TextInput(), initial="123")

    class Meta:
        model = Group
        fields = '__all__'

