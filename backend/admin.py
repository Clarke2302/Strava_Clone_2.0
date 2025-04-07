from django.contrib import admin
from .models import (Atividade, Clube, Equipamento, Perfil, Record)

# Register your models here.

admin.site.register(Atividade)
admin.site.register(Clube)
admin.site.register(Equipamento)
admin.site.register(Perfil)
admin.site.register(Record)