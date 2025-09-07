from django.shortcuts import render
from .models import Product, Order
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

def detail(request, id):
    product = Product.objects.get(id=id)

    return render(request, 'shop/detail.html', {'product': product})

def checkout(request):

    if request.method == "POST":
        items = request.POST.get('items', '')
        firstName = request.POST.get('firstName', '')
        lastName = request.POST.get('lastName', '')
        email = request.POST.get('email', '')
        phoneNumber = request.POST.get('phoneNumber', '')
        address = request.POST.get('address', '')
        state = request.POST.get('state', '')
        city = request.POST.get('city', '')
        zip = request.POST.get('zip', '')
        total = request.POST.get('total', '')
        
        order = Order(items=items, first_name=firstName, last_name=lastName, email=email, mobile_number=phoneNumber, address=address, state=state, city=city, zip=zip, total=total)
        order.save()

    return render(request, 'shop/checkout.html')

