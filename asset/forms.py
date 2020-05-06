from django import forms
from .models import Category, Station, Asset

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['name']


class StationForm(forms.ModelForm):

    class Meta:
        model = Station
        fields = ['name', 'max_cap']


class AssetForm(forms.ModelForm):

    class Meta:
        model = Asset
        fields = ['name']
