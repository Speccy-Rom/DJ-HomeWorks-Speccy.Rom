from django.views.generic import ListView
from django.shortcuts import render

from .models import Article, Scope, Membership


def articles_list(request):
    template = 'articles/news.html'
    context = {}
    articles = Article.objects.all()
    context['tags'] = {}
    for article in articles:
        context['tags'][article.id] = {}
        tags = Scope.objects.filter(article=article.id).order_by('-membership__is_main', 'tematik').all()
        context['tags'][article.id] = tags
    context['object_list'] = Article.objects.all()
    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'

    return render(request, template, context)
