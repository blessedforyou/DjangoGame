from django.contrib import admin
from game import models


# Register your models here.
@admin.register(models.Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ("username", "first_login", "last_login", "points")


@admin.register(models.Boost)
class BoostAdmin(admin.ModelAdmin):

    list_display = ("player", "title", "type", "active", "source", "acquired_at")