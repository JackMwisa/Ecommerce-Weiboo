from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def product_list(request):
    """
    Display all available products, optionally filtered by category slug.
    """
    category_slug = request.GET.get('category')
    products = Product.objects.filter(is_available=True)

    selected_category = None
    if category_slug:
        selected_category = get_object_or_404(Category, slug=category_slug, is_active=True)
        products = products.filter(category=selected_category)

    categories = Category.objects.filter(is_active=True)

    context = {
        'products': products,
        'categories': categories,
        'selected_category': selected_category,
    }
    return render(request, 'store/product_list.html', context)


def product_detail(request, slug):
    """
    Display the detail page of a single product.
    """
    product = get_object_or_404(Product, slug=slug, is_available=True)
    gallery_images = product.images.all()

    context = {
        'product': product,
        'gallery_images': gallery_images,
    }
    return render(request, 'store/product_detail.html', context)
