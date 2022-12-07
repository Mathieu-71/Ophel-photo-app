from django.shortcuts import render
from .models import *
from urllib.parse import urlparse
from django.contrib.admin.views.decorators import staff_member_required




@staff_member_required()
def home(request):
    categories = Category.objects.all()

    context = {'categories': categories}

    return render(request, 'gallery/index.html', context)

@staff_member_required()
def categoryPage(request):
    category = Category.objects.all()
    images = Image.objects.all()



    return render(request, 'gallery/category.html', {'category': category, 'images': images})

@staff_member_required()
def imageDetailPage(request, slug1):
    category = Category.objects.get(slug=slug1)
    images = Image.objects.filter(category=category)
    i = 0
    test_dict ={}
    for im in images:
        test_dict[str(i)] =im
        i += 1
    context = {'category': category, 'images': images,
               'dico':test_dict}

    return render(request, 'gallery/image.html', context)
