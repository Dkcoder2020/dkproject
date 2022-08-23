from django import forms
from newsapp.models import News

class NewsForm(forms.ModelForm):
    class Meta:
        model=News
        fields="__all__"
    