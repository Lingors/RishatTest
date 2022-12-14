from django.db import models

CURRENCIES = (
    ('usd', 'USD'),
    ('eur', 'EUR'),
)


class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField(default=0)
    currency = models.CharField(
        max_length=3,
        choices=CURRENCIES,
        default='usd',
    )


class Discount(models.Model):
    name = models.CharField(max_length=200)
    percent_off = models.FloatField(default=0)


class Tax(models.Model):
    name = models.CharField(max_length=200)
    percentage = models.FloatField(default=0)
    stripe_id = models.CharField(max_length=50, default='', blank=True, null=True)


class Order(models.Model):
    items = models.ManyToManyField(Item)
    discounts = models.ManyToManyField(Discount)
    taxes = models.ManyToManyField(Tax)
    total_price = models.FloatField(default=0)
