from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Item


def item_list(request):
    qs = Item.objects.all()
    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(name__icontains=q)
    return render(request, 'shop/item_list.html', {
        'item_list': qs,
        'q': q,
    })


def item_detail(request, item_id):
    item_detail = get_object_or_404(Item, pk=item_id)
    return render(request, 'shop/detail.html', {'item':item_detail})