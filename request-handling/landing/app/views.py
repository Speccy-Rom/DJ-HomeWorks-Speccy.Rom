from collections import Counter

from django.shortcuts import render_to_response

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()


def index(request):
    # Реализуйте логику подсчета количества переходов с лендига по GET параметру from-landing
    transition = request.GET['from-landing']
    # counter_click(transition)
    if transition == 'original':
        counter_click['original'] += 1
    elif transition == 'test':
        counter_click['test'] += 1
    #       return render_to_response('landing_alternate.html')
    return render_to_response('index.html')


def landing(request):
    # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов
    site = request.GET['ab-test-arg']
    # counter_show(site)
    if site == 'original':
        counter_show['original'] += 1
        return render_to_response('landing.html')
    elif site == 'test':
        counter_show['test'] += 1
        return render_to_response('landing_alternate.html')
    # return render_to_response('landing.html')


def stats(request):
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Чтобы отличить с какой версии лендинга был переход
    # проверяйте GET параметр marker который может принимать значения test и original
    # Для вывода результат передайте в следующем формате:
    if not counter_show['alternative']:
        counter_show['alternative'] = 1
    if not counter_show['original']:
        counter_show['original'] = 1
    return render_to_response('stats.html', context={
        'test_conversion': format(counter_click['alternative'] / counter_show['alternative'], '.1f'),
        'original_conversion': format(counter_click['original'] / counter_show['original'], '.1f'),
    })
