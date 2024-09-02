from django.contrib import admin
from . import models


admin.site.register(models.Player)
admin.site.register(models.PlayerLevel)
admin.site.register(models.Prize)
admin.site.register(models.Level)
admin.site.register(models.LevelPrize)