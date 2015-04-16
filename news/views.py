from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import News


def index(request):
    latest_news_list = News.objects.order_by('-pub_date')[:10]
    template = loader.get_template('news/index.html')
    context = RequestContext(request, {
        'latest_news_list': latest_news_list,
    })
    return HttpResponse(template.render(context))


def detail(request, news_id):
    pass