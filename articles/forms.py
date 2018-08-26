from django import forms


class ProfileForm(forms.Form):
    title = forms.CharField(max_length=10000)
    content = forms.CharField(max_length=10000)
    picture = forms.ImageField()
