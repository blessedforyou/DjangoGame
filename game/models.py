from django.db import models
from django.utils import timezone


# Create your models here.
class Player(models.Model):
    username = models.CharField(max_length=32, unique=True, verbose_name="Имя")
    first_login = models.DateTimeField(null=True, blank=True, verbose_name="Первый вход")
    last_login = models.DateTimeField(null=True, blank=True, verbose_name="Последний вход")
    points = models.IntegerField(default=0, verbose_name="Очки")


    def save(self, *args, **kwargs):
        now = timezone.now()
        if not self.first_login:
            self.first_login = now
        if now.date() > self.last_login.date():
            self.points += 10

        self.last_login = now
        super(Player, self).save(*args, **kwargs)


    def add_boost(self, boost_title, boost_type, source="manually"):
        boost = Boost.objects.create(player=self, title=boost_title, type=boost_type, source=source)
        return boost


    class Meta:
        ordering = ('id', )
        verbose_name = "Игрок"
        verbose_name_plural = "Игроки"    

    def __str__(self):
        return self.username


class Boost(models.Model):
    SOURCE_BOOST = (
        ('level', 'Пройденный уровень'),
        ('manually', 'Вручную')
    )

    title = models.CharField(max_length=20, verbose_name="Название буста")
    type = models.CharField(max_length=15, verbose_name="Тип буста")
    player = models.ForeignKey(to=Player, on_delete=models.CASCADE, verbose_name="Игрок")
    active = models.BooleanField(default=False, verbose_name="Активен")
    source = models.CharField(max_length=8, choices=SOURCE_BOOST, verbose_name="Источник получения")
    acquired_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата получения")


    class Meta:
        ordering = ('id', )
        verbose_name = "Буст"
        verbose_name_plural = "Бусты"

    def __str__(self):
        return f"{self.title} ({self.type})"
    
