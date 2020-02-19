from django.test import TestCase
from .models import Currency
import datetime


class CurrencyAddTestCase(TestCase):
    def setUp(self) -> None:
        Currency.objects.create(code='USD', buy_rate=19, sale_rate=20, start_date=datetime.date(2020, 2, 10))
        Currency.objects.create(code='USD', buy_rate=20, sale_rate=21, start_date=datetime.date(2020, 2, 13))

    def test_currency_add(self):
        new_obj = Currency.objects.create(code='USD', buy_rate=21, sale_rate=22, start_date=datetime.date.today())

        prev_obj = Currency.objects.filter(start_date__lt=new_obj.start_date).order_by('-start_date').first()
        # prev_obj = Currency.objects.get(start_date=datetime.date(2020, 2,13)) # another way to get same obj

        self.assertEqual(prev_obj.end_date, new_obj.start_date - datetime.timedelta(days=1))


class CurrencyInsertTestCase(TestCase):
    def setUp(self) -> None:
        Currency.objects.create(code='USD', buy_rate=19, sale_rate=20, start_date=datetime.date(2020, 2, 1))
        Currency.objects.create(code='USD', buy_rate=20, sale_rate=21, start_date=datetime.date(2020, 2, 14))

    def test_currency_insert(self):
        new_obj = Currency.objects.create(code='USD', buy_rate=21, sale_rate=22, start_date=datetime.date(2020, 2, 10))

        prev_obj = Currency.objects.filter(start_date__lt=new_obj.start_date).order_by('-start_date').first()
        # prev_obj = Currency.objects.get(start_date=datetime.date(2020, 2, 1))

        next_obj = Currency.objects.filter(start_date__gt=new_obj.start_date).order_by('start_date').first()
        # next_obj = Currency.objects.get(start_date=datetime.date(2020, 2, 14))

        self.assertEqual(new_obj.end_date, next_obj.start_date - datetime.timedelta(days=1))
        self.assertEqual(prev_obj.end_date, new_obj.start_date - datetime.timedelta(days=1))


class CurrencyDeleteTestCase(TestCase):
    def setUp(self) -> None:
        Currency.objects.create(code='USD', buy_rate=19, sale_rate=20, start_date=datetime.date(2020, 2, 10))
        Currency.objects.create(code='USD', buy_rate=20, sale_rate=21, start_date=datetime.date(2020, 2, 13))
        Currency.objects.create(code='USD', buy_rate=21, sale_rate=22, start_date=datetime.date(2020, 2, 20))

    def test_currency_delete(self):
        obj = Currency.objects.get(start_date=datetime.date(2020, 2, 13))
        obj.delete()

        prev_obj = Currency.objects.filter(start_date__lt=obj.start_date).order_by('-start_date').first()
        # prev_obj = Currency.objects.get(start_date=datetime.date(2020, 2,10))

        self.assertEqual(prev_obj.end_date, obj.end_date)
