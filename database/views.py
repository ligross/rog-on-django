from django.shortcuts import render, get_object_or_404

from .models import ResourceNode

def resources(request):
    resources_list = ResourceNode.objects.order_by('-node_name')
    context = {'resources_list': resources_list}
    return render(request, 'database/resources.html', context)
