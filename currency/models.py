import datetime
from django.db import models


class Currency(models.Model):
    currency_code_choices = [
        ('USD', 'USD'),
        ('EUR', 'EUR'),
        ('RUB', 'RUB'),
    ]
    code = models.CharField(max_length=3, choices=currency_code_choices)
    sale_rate = models.DecimalField(max_digits=10, decimal_places=2)
    buy_rate = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField(db_index=True, default=datetime.date.today)
    end_date = models.DateField(blank=True, null=True)

    def save(self, *args, **kwargs):
        try:  # check next date in history
            next_obj = Currency.objects.filter(start_date__gt=self.start_date, code=self.code)\
                .order_by('start_date').first()
            self.end_date = next_obj.start_date - datetime.timedelta(days=1)
        except:
            """added latest object"""

        try:  # check previous date in history
            prev_obj = Currency.objects.filter(start_date__lt=self.start_date, code=self.code)\
                .order_by('-start_date').first()
            prev_obj.end_date = self.start_date - datetime.timedelta(days=1)
            super(Currency, prev_obj).save()
        except:
            """added earliest object"""

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        try:
            obj = Currency.objects.filter(start_date__lt=self.start_date, code=self.code)\
                .order_by('-start_date').first()
            obj.end_date = self.end_date
            super(Currency, obj).save()
        except:
            """deleted earliest object"""
