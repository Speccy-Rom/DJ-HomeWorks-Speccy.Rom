from django.contrib import admin
from django.contrib import admin

from .models import Game, Player, PlayerGameInfo


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('player_id',)


class GameAdmin(admin.ModelAdmin):
    list_display = ('game_id', 'number', 'display_players', 'is_finished')


class PlayerGameInfoAdmin(admin.ModelAdmin):
    list_display = ('game_id', 'player_id', 'move_count', 'game_creater', 'game_finished')


admin.site.register(Game, GameAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(PlayerGameInfo, PlayerGameInfoAdmin)