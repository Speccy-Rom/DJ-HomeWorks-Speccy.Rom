from django import forms


class NumberSendPost(forms.Form):
    number = forms.IntegerField(label="Число", widget=forms.TextInput(attrs={'size': '5'}))