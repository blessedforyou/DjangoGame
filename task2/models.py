from django.db import models
from django.utils import timezone


class Player(models.Model):
    player_id = models.CharField(max_length=100)
    
    
class Level(models.Model):
    title = models.CharField(max_length=100)
    order = models.IntegerField(default=0)
    
    
    
class Prize(models.Model):
    title = models.CharField(max_length=32)
    
    
class PlayerLevel(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    completed = models.DateField()
    is_completed = models.BooleanField(default=False)
    score = models.PositiveIntegerField(default=0)

    def get_prize(self):

        if not self.is_completed:
            raise ValueError("Уровень не завершен.")
        
        unreceived_prizes = LevelPrize.objects.filter(level=self.level, received__isnull=True)
        
        if not unreceived_prizes.exists():
            raise ValueError("Призы за данный уровень уже были получены")
        
        level_prizes = LevelPrize.objects.filter(level=self.level)
        for level_prize in level_prizes:
            level_prize.received = timezone.now()
            level_prize.save()

    
class LevelPrize(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    prize = models.ForeignKey(Prize, on_delete=models.CASCADE)
    received = models.DateField()
     
     