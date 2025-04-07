from django.utils.translation import gettext_lazy as _
from django.db import models

class TipoEquipamento(models.TextChoices):
    SNEAKER = "Tênis", _("Tênis")
    BIKE = "Bicicleta", _("Bicicleta")
    SMART_DEVICE = "Dispositivo_inteligente", _("Dispositivo Inteligente")

