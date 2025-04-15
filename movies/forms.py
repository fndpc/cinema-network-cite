from django import forms

class OrderForm(forms.Form):
    film = forms.CharField(max_length=10)

    