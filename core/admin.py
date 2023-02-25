from django.contrib import admin
from .models import Cargo, Servico, Time


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'ativo', 'modificado')


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servico', 'icone', 'ativo', 'modificado')


@admin.register(Time)
class TimeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'modificado', 'ativo')





