from django.contrib import admin
from madness.models import Bracket, Entry, EntryPick, Game, Region, Team

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
	pass


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
	pass


@admin.register(Bracket)
class BracketAdmin(admin.ModelAdmin):
	pass


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
	pass


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
	pass


@admin.register(EntryPick)
class EntryPickAdmin(admin.ModelAdmin):
	pass