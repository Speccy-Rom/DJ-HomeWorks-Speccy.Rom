from django import template
from datetime import datetime, timedelta

register = template.Library()


@register.filter
def format_date(value):
    # Ваш код
    date = datetime.fromtimestamp(int(value))
    date_now = datetime.today()
    res = date_now - date
    if res.total_seconds() / 60 < 10:
        return 'Только что'
    elif res.total_seconds() / 60 > 10 and res.total_seconds() / 3600 < 24:
        return f'{int(res.total_seconds() / 3600)} часов назад'
    else:
        return date


# необходимо добавить фильтр для поля `score`


@register.filter
def format_num_comments(value):
    # Ваш код
    if int(value) <= -5:
        return 'Все плохо'
    elif int(value) > -5 and int(value) <= 5:
        return 'Нейтрально'
    else:
        return 'Хорошо'


@register.filter
def format_num_comments(value):
    if int(value) == 0:
        return 'Остаьвте комментарий'
    elif int(value) > 0 and int(value) <= 50:
        return value
    else:
        return '50+'


@register.filter
def format_selftext(value, count):
    if value == '':
        return ''
    else:
        value = value.split(' ')
        if len(value) > 2 * count:
            start = ' '.join(value[0:count])
            end = value[-count:]
            end = ' '.join(end)
            return f'{start} ... {end}'
        elif len(value) == 1:
            return f'{value[0]}'
        else:
            count = int(len(value) / 2)
            start = ' '.join(value[0:count])
            end = value[-count:]
            end = ' '.join(end)
            if count == 1:
                return f'{start} {end}'
            else:
                return f'{start} ... {end}'




