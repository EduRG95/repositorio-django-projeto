from django.shortcuts import render

from recipes.models import Recipe
from utils.recipes.factory import make_recipe


# Create your views here.
def home(request):
    # essa função abaixo chama todas as receitas la do models,
    # foram importadas e ordenadas agora de tras para frente com o
    # simbolo - antes do id
    recipes = Recipe.objects.all().order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })


def category(request, category_id):
    recipes = Recipe.objects.filter(
        category__id=category_id
        ).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True,
    })
