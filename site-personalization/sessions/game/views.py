from django.shortcuts import render
from .models import Player, Game, PlayerGameInfo
import random
from django.shortcuts import redirect
from .forms import NumberSendPost


def show_home(request):
    number = random.randint(0, 10)  # генерируем число для игры
    ids_generated = random.randint(0, 1000)  # генерируем число для айдишников

    if request.session.get('player_id') and request.session.get('game_id'):
        # смотрим на сессию на наличие идентификаторов игры и юзера
        cur_game = Game.objects.get(game_id=request.session.get('game_id'))
        if cur_game.is_finished:
            if Game.objects.filter(is_finished=False).count() == 0:
                new_game = Game.objects.create(is_finished=False, number=random.randint(0, 10))
                cur_player = Player.objects.get(player_id=request.session.get('player_id'))
                new_game.player.add(cur_player)
                player_game_info_add(new_game, cur_player, 0, True, True)
                request.session['game_id'] = str(new_game.game_id)
                return redirect('/')
            else:
                cur_game = Game.objects.get(is_finished=False)
                cur_player = Player.objects.get(player_id=request.session.get('player_id'))
                cur_game.player.add(cur_player)
                player_game_info_add(cur_game, cur_player, 0, False, False)
                request.session['game_id'] = str(cur_game.game_id)
                return redirect('/')
        else:
            cur_player = Player.objects.get(player_id=request.session.get('player_id'))
            if PlayerGameInfo.objects.get(game_id=cur_game, player_id=cur_player).game_creater:
                return redirect('game-creator')
            else:
                return redirect('game-play')
    else:
        # если сесия новая.....
        # если нет активных игр создаем новую игру и нового игрока
        if Game.objects.filter(is_finished=False).count() == 0:
            new_game = Game.objects.create(is_finished=False, number=number)
            new_player = Player.objects.create(player_id=f'p{ids_generated}')
            new_game.player.add(new_player)
            player_game_info_add(new_game, new_player, 0, True, True)
            request.session['player_id'] = f'p{ids_generated}'
            request.session['game_id'] = str(new_game.game_id)
            return redirect('/')
        else:
            # если есть активная игра создаем игрока и присоединяем его к игре
            cur_game = Game.objects.get(is_finished=False)
            new_player = Player.objects.create(player_id=f'p{ids_generated}')
            cur_game.player.add(new_player)
            player_game_info_add(cur_game, new_player, 0, False, False)
            request.session['player_id'] = f'p{ids_generated}'
            request.session['game_id'] = str(cur_game.game_id)
            return redirect('/')


def show_game_creator(request):
    cur_game = Game.objects.get(game_id=request.session.get('game_id'))
    cur_player = Player.objects.get(player_id=request.session.get('player_id'))
    context = {}

    # список игроков завершивших игру на данный момент
    players_finished_game = PlayerGameInfo.objects \
        .filter(game_id=cur_game) \
        .exclude(player_id=cur_player) \
        .filter(game_finished=True)

    if players_finished_game:
        context['players_win'] = players_finished_game

    # определяем конец игры когда все игроки отгадали число
    # еденица на случай если игроков нет )))
    finished_players = PlayerGameInfo.objects.filter(game_id=cur_game).filter(game_finished=True).count()
    all_players = PlayerGameInfo.objects.filter(game_id=cur_game).count()

    if all_players == finished_players != 1:
        context['game_over'] = True
        cur_game.is_finished = True
        cur_game.save()

    context['number'] = cur_game.number
    return render(
        request,
        'game_creator.html',
        context
    )


def show_game_play(request):
    cur_game = Game.objects.get(game_id=request.session.get('game_id'))
    cur_player = Player.objects.get(player_id=request.session.get('player_id'))
    counter = PlayerGameInfo.objects.filter(game_id=cur_game).get(player_id=cur_player)
    form = NumberSendPost(request.POST or None)
    context = {}

    if form.is_valid():
        answer = int(request.POST.get('number'))
        if answer == cur_game.number:
            counter.game_finished = True
            context['text'] = 'Вы угадали число!'
            context['game_over'] = True
        elif answer < cur_game.number:
            context['text'] = f'Загаданное число больше числа {answer}'
        elif answer > cur_game.number:
            context['text'] = f'Загаданное число меньше числа {answer}'
        counter.move_count += 1
        counter.save()
        context['form'] = form
        return render(request, 'game_play.html', context)
    else:
        context['form'] = form
        return render(request, 'game_play.html', context)


def player_game_info_add(game, player, count, created, finished):
    PlayerGameInfo.objects.create(
        game_id=game,
        player_id=player,
        move_count=count,
        game_creater=created,
        game_finished=finished
    )
