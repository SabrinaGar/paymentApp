import uuid
from django.db import models

class Payment(models.Model):
    """
    Representa una transacción de pago entre un remitente y un receptor.

    Este modelo almacena los detalles de un pago, incluyendo los montos y las
    monedas de origen y destino, los países involucrados, y el estado del pago.
    También registra la fecha de creación y la última actualización de la transacción.

    Campos:
    - id: Un identificador único para la transacción de pago.
    - source_amount: El monto de dinero que se envía.
    - source_currency: La moneda del monto de origen (ej. USD, EUR).
    - source_country: El país de origen (remitente).
    - target_amount: El monto de dinero recibido.
    - target_currency: La moneda del monto recibido (ej. USD, EUR).
    - target_country: El país de destino (receptor).
    - created: La fecha y hora cuando se creó el pago.
    - updated: La fecha y hora cuando se actualizó el pago por última vez.
    - status: El estado actual del pago (ej. Draft, Requested, Approved, Paid).
    - concept: Una descripción opcional de la transacción de pago.
    - rate_exchange: La tasa de cambio aplicada al pago.
    - sender_full_name: El nombre completo del remitente.
    - receiver_full_name: El nombre completo del receptor.
    """
    STATUS_CHOICES = [
        ('Draft', 'Draft'),
        ('Requested', 'Requested'),
        ('Approved', 'Approved'),
        ('Paid', 'Paid'),
        ('Deleted', 'Deleted'),
    ]

    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    source_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    source_currency = models.CharField(max_length=3)
    source_country = models.CharField(max_length=2)
    target_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    target_currency = models.CharField(max_length=3)
    target_country = models.CharField(max_length=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Draft')
    concept = models.CharField(max_length=255, null=True, blank=True)
    rate_exchange = models.DecimalField(max_digits=10, decimal_places=6, default=0)
    sender_full_name = models.CharField(max_length=255, default='')
    receiver_full_name = models.CharField(max_length=255, default='')

    def __str__(self):
        return f"{self.source_amount} {self.source_currency} to {self.target_amount} {self.target_currency}"
