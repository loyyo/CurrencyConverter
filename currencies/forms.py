from django import forms


class CurrencyForm(forms.Form):
    currency_one = forms.CharField(max_length=3)
    amount = forms.FloatField()
    currency_two = forms.CharField(max_length=3)
