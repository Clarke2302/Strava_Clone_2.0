from django.utils.translation import gettext_lazy as _
from django.db import models

class TipoEsporte(models.TextChoices):
    RUN = "Corrida", _("Corrida")
    TRAIL_RUN = "Corrida de Trilhas", _("Corrida de Trilhas")
    BIKE = "Treino de Bicicleta", _("Treino de Bicicleta")
    WALK = "Caminhada", _("Caminhada")
    HIIT = "Treino de Alta Intensidade", _("Treino de Alta Intensidade")
    STRENGTH = "Treino de Força", _("Treino de Força")
    CARDIO = "Treino Aeróbico", _("Treino Aeróbico")
    SWIMMING = "Natação", _("Natação")





