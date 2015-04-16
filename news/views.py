from django.http import HttpResponse

from .models import News


def index(request):
    latest_news_list = News.objects.order_by('-pub_date')[:10]
    output = ', '.join([news.news_title for news in latest_news_list])
    return HttpResponse(output)


def detail(request, news_id):
    pass