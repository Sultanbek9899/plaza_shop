from backend.apps.products.models import Category

def get_category(request):
    categories = Category.objects.all()
    context = {"categories": categories}
    return context