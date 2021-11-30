from django import forms

class NameForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Search', 'style': 'width: 300px;', 'class': 'form-control me-2'}))

class CommentForm(forms.Form):
    your_comment = forms.CharField(label='Your comment', max_length=500, widget=forms.Textarea)