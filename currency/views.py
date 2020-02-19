import datetime
from django.shortcuts import render
from django.views.generic import ListView, View
from .models import Currency
from django.http import Http404


class CurrencyListView(ListView):
    template_name = 'currency/list.html'
    model = Currency
    context_object_name = 'currencies'

    def get_queryset(self):
        # sqlite doesn't support DISTINCT
        # return Currency.objects.filter(start_date__gte=datetime.date.today()).order_by('start_date').distinct('code')

        return filter(None, (Currency.objects.filter(start_date__gte=datetime.date.today(), code=code)
            .order_by('start_date').first() for code in ['USD', 'EUR', 'RUB']))


class CurrencyHistory(View):
    def get(self, request, *args, **kwargs):
        if kwargs.get('code') not in ['usd', 'eur', 'rub']:
            raise Http404

        code = kwargs.get('code')
        records = Currency.objects.filter(code=code.upper()).order_by('start_date')

        return render(request, 'currency/history.html', {'records': records, 'code': code})


