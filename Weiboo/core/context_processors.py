from store.models import Category

def categories_processor(request):
    return {
        'main_categories': Category.objects.filter(parent=None, is_active=True)
    }
