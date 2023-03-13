from django.db import models
from django.db.models import PositiveSmallIntegerField


class DateModel(models.Model):
    class Meta:
        abstract = True

    created = models.DateTimeField(verbose_name='created at', auto_now_add=True)


class Contact(models.Model):
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    email = models.EmailField('email', null=True, blank=True, unique=True)
    country = models.CharField('country', max_length=50, null=True, blank=True)
    city = models.CharField('city', max_length=50, null=True, blank=True)
    street = models.CharField('street', max_length=50, null=True, blank=True)
    house_number = models.CharField('house_number', max_length=10, null=True, blank=True)

    def __str__(self):
        return f'{self.country}, {self.city}, {self.street}, {self.house_number}'


class Product(models.Model):
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    title = models.CharField('title', max_length=255)
    model = models.CharField('model', max_length=255, null=True, blank=True)
    release_date = models.DateField('release date', null=True, blank=True)

    def __str__(self):
        return self.title


class Provision(models.Model):
    class Meta:
        verbose_name = 'Provision'
        verbose_name_plural = 'Provisions'

    class SupType(models.IntegerChoices):
        manufacturer = 0, 'Manufacturer'
        reseller = 1, 'Reseller'
        retailer = 2, 'Retailer'

    title = models.CharField(verbose_name='title', max_length=64)
    type = PositiveSmallIntegerField(
        verbose_name='Supplier type', choices=SupType.choices, default=SupType.manufacturer
    )

    def __str__(self):
        return self.title


class Retail(DateModel):
    class Meta:
        verbose_name = 'Retail'
        verbose_name_plural = 'Retails'

    title = models.CharField(verbose_name='title', max_length=255, unique=True)
    contact = models.ForeignKey(
        Contact, verbose_name='contact', on_delete=models.PROTECT, related_name='links', null=True, blank=True
    )
    product = models.ForeignKey(
        Product, verbose_name='product', on_delete=models.PROTECT, related_name='retailers', null=True, blank=True
    )
    provision = models.ForeignKey(
        Provision, verbose_name='provision', on_delete=models.PROTECT, related_name='distributors', null=True, blank=True
    )
    receivables = models.DecimalField(verbose_name='receivables, RUB', max_digits=11, decimal_places=2, default=0)

    def __str__(self):
        return self.title
