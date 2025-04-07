from django.utils.translation import gettext_lazy as _
from django.db import models

class TipoMarca(models.TextChoices):
    CEM_METROS = "100M", _("100 Metros")
    QUATROCENTROS_METROS = "400M", _("400 Metros")
    UM_KM = "1KM", _("1 Quilômetro")
    CINCO_KM = "5KM", _("5 Quilômetros")
    DEZ_KM = "10KM", _("10 Quilômetros")
    QUINZE_KM = "15KM", _("15 Quilômetros")
    VINTE_KM = "20KM", _("20 Quilômetros")
    MEIA = "Meia Maratona", _("Meia Maratona")
    TRINTA_KM = "30KM", _("30 Quilômetros")
    MARATONA = "Maratona", _("Maratona")
    LONGA_DISTANCIA = "Longa Distância", _("Longa Distância")
    LONGA_DURACAO = "Longa Duração", _("Longa Duração")






