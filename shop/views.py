from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator

def index(request):
    products = Product.objects.all()

    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        products = products.filter(name__icontains=item_name)

    paginator = Paginator(products, 12) 
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    return render(request, 'shop/index.html', {'products': products})

