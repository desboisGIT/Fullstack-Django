from django.shortcuts import render, redirect
from .forms import RecipeForm
from Recipes.models import Recipe
from Recipes.urls import details
# Create your views here.

def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.author = request.user
            temp.save()
            return redirect(details, id=temp.id)
        else:
            return render(request, 'recipe_form.html', {'form': form})
    else:
        form = RecipeForm()
        return render(request, 'recipe_form.html', {'form': form})
    
def recipe_delete(request, id):
    if request.user.is_authenticated:
        recipe = Recipe.objects.get(id=id)
        if request.user == recipe.author:
            recipe.delete()
            return redirect('recipes')
        else:
            return redirect('details', id=id)
    else:
        return redirect('login')
