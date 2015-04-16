from django.http import HttpResponse

from .models import Article


def latest(request):
    latest_articles_list = Article.objects.order_by('-pub_date')[:10]
    output = ', '.join([article.article_title for article in latest_articles_list])
    return HttpResponse(output)


def detail(request, article_id):
    pass