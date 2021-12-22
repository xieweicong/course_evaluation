from django import forms


class SearchForm(forms.Form):
    searchCourse = forms.CharField()
