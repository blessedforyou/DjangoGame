import csv

from django.http import HttpResponse
from django.shortcuts import render
from .models import PlayerLevel, LevelPrize


def some_view(request):
    response = HttpResponse(
        content_type="text/csv",
        headers={"Content-Disposition": 'attachment; filename="player_levels.csv"'},
    )

    writer = csv.writer(response)
    writer.writerow(["Player ID", "Level Name", "Level Status", "Level Prize"])

    player_levels = PlayerLevel.objects.select_related("player", "level").iterator()

    for player_level in player_levels:
        level_prizes = LevelPrize.objects.filter(level=player_level.level, received__isnull=False)
        prizes = ", ".join(prize.prize.title for prize in level_prizes)

        writer.writerow([player_level.player.player_id, 
                        player_level.level.title,
                        "Yes" if player_level.is_completed else "No", 
                        prizes if prizes else "No prizes"])
    
    return response