from core.abstract.models import AbstractModel, AbstractManager
from django.db import models


class CounterpartyManager(AbstractManager):
    pass


class Counterparty(AbstractModel):
    CLIENT = 'client'
    SUPPLIER = 'supplier'

    COUNTERPARTY_TYPE_CHOICES = [

        (CLIENT, 'Клиент'),
        (SUPPLIER, 'Поставщик'),
    ]

    name = models.CharField(max_length=255, verbose_name='name')
    type = models.CharField(max_length=255, choices=COUNTERPARTY_TYPE_CHOICES, verbose_name='type')
    contact_phone = models.CharField(max_length=255, verbose_name='phone')
    contact_email = models.CharField(max_length=255, verbose_name='email')
    address = models.CharField(max_length=255, verbose_name='address')
    manager = models.CharField(max_length=255, verbose_name='manager')
    note = models.TextField(verbose_name='note')
    owner = models.ForeignKey('core_user.User', on_delete=models.CASCADE, verbose_name='owner')
    objects = CounterpartyManager()

    class Meta:
        verbose_name = 'Counterparty'
        verbose_name_plural = 'Counterparties'
        db_table = 'counterparties'
    
    def __str__(self):
        return self.name



