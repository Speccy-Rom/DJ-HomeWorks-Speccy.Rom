from django.shortcuts import render
from .models import Article, Profile

def show_articles(request):
    art = Article.objects.all()
    return render(
        request,
        'articles.html',
        {'art': art}
    )


def show_article(request, id):
    obj = Article.objects.get(id=id)
    user = request.user
    prof = Profile.objects.get(user=user).has_subcription
    if obj.pay_article and not prof:
        context = {'title': obj.title, 'limited': 'Статья платная, пожалуйста, подпишитесь'}
    else:
        context = {'title': obj.title, 'body': obj.text}
    return render(
        request,
        'article.html',
        context
    )
