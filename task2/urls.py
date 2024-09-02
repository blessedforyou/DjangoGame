from django.urls import path
from . import views

urlpatterns = [
    path("export/player-data/", views.some_view, name="export_player_data")
]