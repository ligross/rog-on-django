from django.shortcuts import render, get_object_or_404

from .models import Article


def latest(request):
    latest_articles_list = Article.objects.order_by('-pub_date')[:10]
    context = {'latest_articles_list': latest_articles_list}
    return render(request, 'articles/articles.html', context)


def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'articles/detail.html', {'article': article})