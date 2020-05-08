from .models import Activity
from django import forms
from asset.models import Asset

class ActivityForm(forms.ModelForm):

    class Meta:
        model = Activity
        fields = ['asset', 'station']

class AssetForm(forms.ModelForm):

    class Meta:
        model = Activity
        fields = ['asset']
