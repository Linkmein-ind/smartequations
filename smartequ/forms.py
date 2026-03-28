from django import forms
from .models import RequestCall

class RequestCallForm(forms.ModelForm):

    class Meta:
        model = RequestCall
        fields = ['name', 'mobile', 'email', 'message']