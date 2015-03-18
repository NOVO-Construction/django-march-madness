from django.contrib import admin
from django.db.models import Count

from core.admin import RelatedFieldAdmin

from . import models


@admin.register(models.Region)
class RegionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Team)
class TeamAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Bracket)
class BracketAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Game)
class GameAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Entry)
class EntryAdmin(RelatedFieldAdmin):
    list_display = ('name', 'user__first_name', 'user__last_name', 'user__email', 'entrypick_count')
    list_select_related = ('user',)

    def queryset(self, request):
        return models.Entry.objects.annotate(entrypick_count=Count('entrypick'))

    def entrypick_count(self, inst):
        return inst.entrypick_count
    entrypick_count.admin_order_field = 'entrypick_count'


@admin.register(models.EntryPick)
class EntryPickAdmin(RelatedFieldAdmin):
    list_display = ('pick', 'entry__name', 'entry__user__first_name', 'entry__user__last_name', 'entry__user__username')
    list_select_related = ('entry__user', 'pick__team')
