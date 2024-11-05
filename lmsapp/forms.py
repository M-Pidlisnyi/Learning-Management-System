from django import forms
from .models import Group

class GroupForm(forms.ModelForm):
    codename = forms.CharField(widget=forms.TextInput())
    start_date = forms.DateTimeField(
                widget=forms.DateTimeInput(attrs={"type":"datetime-local"}),
                required=False)

    class Meta:
        model = Group
        fields = '__all__'

