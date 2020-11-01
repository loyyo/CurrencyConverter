from django.views.generic import TemplateView
from django.shortcuts import render
from .forms import CurrencyForm
from .templatetags.convert import convert


class HomeView(TemplateView):
    template_name = 'base.html'

    def get(self, request):
        form = CurrencyForm()
        value = 0
        context = {'form': form, 'value': value}
        return render(request, self.template_name, context)

    def post(self, request):
        form = CurrencyForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['currency_one']
            amount = form.cleaned_data['amount']
            b = form.cleaned_data['currency_two']
            value = convert(a, b, amount)
        context = {'form': form, 'value': value,
                   'a': a, 'b': b, 'amount': amount}
        return render(request, self.template_name, context)
