from . models import Category

# def common(request):
#     context = {
#     'category_list':Category.objects.all(),
#     }
#     return context

def common(request):
    context = {
    'category_list':Category.objects.all(),
    }
    return context
