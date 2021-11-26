from django import forms

class NameForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Search', 'style': 'width: 300px;', 'class': 'form-control me-2'}))