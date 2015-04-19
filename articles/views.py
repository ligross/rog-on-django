from django.shortcuts import render

from .models import Article

def latest(request):
    latest_articles_list = Article.objects.order_by('-pub_date')[:10]
    output = ', '.join([article.article_title for article in latest_articles_list])
    return render(output)


def detail(request, article_id):
    pass