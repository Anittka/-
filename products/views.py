from django.shortcuts import render
from .models import Product


def product_list(request):

    query = request.GET.get('q')
    sort = request.GET.get('sort')
    supplier = request.GET.get('supplier')

    products = Product.objects.all()

    if query:
        products = products.filter(
            name__icontains=query
        )

    if supplier:
        products = products.filter(
            supplier=supplier
        )

    if sort == "price":
        products = products.order_by("price")

    if sort == "-price":
        products = products.order_by("-price")

    return render(
        request,
        'products/product_list.html',
        {
            'products': products
        }
    )