from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .forms import CurrencyForm
from .templatetags.convert import convert
from forex_python.bitcoin import BtcConverter


def handler404(request, exception=None):
    return redirect('/')


class HomeView(TemplateView):
    template_name = 'base.html'

    def get(self, request):
        try:
            form = CurrencyForm()
            value = 0
            btc = BtcConverter()
            price = round(btc.get_latest_price('PLN'), 2)
            context = {'form': form, 'value': value, 'price': price}
            return render(request, self.template_name, context)
        except:
            return redirect('/')

    def post(self, request):
        try:
            form = CurrencyForm(request.POST)
            if form.is_valid():
                a = form.cleaned_data['currency_one'].upper()
                amount = form.cleaned_data['amount']
                b = form.cleaned_data['currency_two'].upper()
                value = convert(a, b, amount)
                btc = BtcConverter()
            price = round(btc.get_latest_price('PLN'), 2)
            context = {'form': form, 'value': value,
                       'a': a, 'b': b, 'amount': amount, 'price': price}
            return render(request, self.template_name, context)
        except:
            return redirect('/')
