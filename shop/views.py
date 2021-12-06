from django.shortcuts import render
from.models import Products
from django.core.paginator import Paginator
# Create your views here.


def index(request):
    product_object = Products.objects.all()
    
    #search code
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_object = product_object.filter(title__icontains = item_name)
    
    #paginator code
    paginator = Paginator(product_object, 3)
    page = request.GET.get('page')
    product_object = paginator.get_page(page)
    return render(request, 'shop/index.html', {'product_object' : product_object})