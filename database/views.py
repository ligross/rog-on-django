from django.shortcuts import render, get_object_or_404

from .models import Page


def content_page(request):
    page = get_object_or_404(Page, pk=1)
    return render(request, 'database/page.html', {'page': page})


def page(request, page_id):
    page = get_object_or_404(Page, pk=page_id)
    return render(request, 'database/page.html', {'page': page})
