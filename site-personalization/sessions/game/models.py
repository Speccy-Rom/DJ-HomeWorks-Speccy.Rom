from django.db import models
import uuid


class Player(models.Model):
    player_id = models.CharField(max_length=100, verbose_name='идентефикатор игрока')

    def __str__(self):
        return self.player_id

class Game(models.Model):
    game_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name='Название')
    # game_id = models.CharField(max_length=100, verbose_name='Название')
    is_finished = models.BooleanField(verbose_name='Игра завершена')
    player = models.ManyToManyField(Player, related_name='game', verbose_name='Игрок')
    number = models.IntegerField()

    def __str__(self):
        return str(self.game_id)

    def display_players(self):
        """
        Создаем список игроков для админки ограничим 5 первыми
        """
        return ', '.join([tag.player_id for tag in self.player.all()[:5]])

    display_players.short_description = 'Игроки'

class PlayerGameInfo(models.Model):
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE, verbose_name='id игры')
    player_id = models.ForeignKey(Player, on_delete=models.CASCADE, verbose_name='id игрока')
    move_count = models.IntegerField(verbose_name='Попытки')
    game_creater = models.BooleanField(verbose_name='Создатель игры')
    game_finished = models.BooleanField(verbose_name='Завершил игру')
