from django import forms
from .models import Deal


class dealsForm(forms.ModelForm):
    class Meta:
        model = Deal
        fields = ['product', ]
