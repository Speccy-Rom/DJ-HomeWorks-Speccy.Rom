from django import template

register = template.Library()


@register.filter
def background(value):
    if value:
        value = float(value)
        if value < 0:
            return '#03fc0f'
        elif value >= 1 and value < 2:
            return '#f7c6c6'
        elif value >= 2 and value < 5:
            return '#f57171'
        elif value >= 5 and value < 1500:
            return '#fc0313'
        else:
            return ''