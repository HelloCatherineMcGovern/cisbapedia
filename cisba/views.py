from django.shortcuts import render
from .models import Category
# Create your views here.

def index(request):
# The homepage for CISBA
    return render(request, 'cisba/index.html')

def categories(request):
    # Show all categories
    categories = Category.objects.order_by('date_added')
    context = {'categories':categories}
    return render(request, 'cisba/categories.html', context)