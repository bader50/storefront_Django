from django.shortcuts import render
from django.db.models import F
from store.models import Product
from store.models import OrderItem
from store.models import Order


def say_hello(request):
    # query_set = Product.objects.filter(
    #     id=F('orderitem__product_id')).order_by('title').values('id', 'title', 'orderitem__product_id').distinct()

    query_set = Order.objects.select_related(
        'customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]

    print(list(query_set)[1].orderitem_set)
    return render(request, 'hello.html', {'name': 'Mosh', 'orders': list(query_set)})
