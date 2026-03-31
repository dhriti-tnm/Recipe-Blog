from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from .models import Recipe

# Create your views here.
def register_view(request):
    if request.method == "POST":
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        username = request.POST.get('uname')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
        else:
            User.objects.create_user(first_name=first_name, last_name=last_name,username=username, email=email, password=password)
            messages.success(request, "Registration successful! You can login now.")
            return redirect('login')
    return render(request, 'register.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, f"Welcome {user.username}!")
            return redirect('recipe_list')  # Or home page
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('/')

@login_required
def recipes(request):
    if request.method == 'POST':
        data = request.POST
        recipe_name = data.get('recipe_name')
        recipe_desc = data.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')
        print("name", recipe_name)
        print("desc", recipe_desc)
        print("iamge", recipe_image)

        Recipe.objects.create(
            recipe_name= recipe_name, 
            recipe_description= recipe_desc, 
            recipe_image= recipe_image)
        messages.success(request, 'Recipe created successfully!')
        return redirect('recipe_list')
    
    return render(request, "recipes.html")

def all_recipes(request):
    query = request.GET.get('q', '')
    if query:
        recipes = Recipe.objects.filter(
            Q(recipe_name__icontains=query) | Q(recipe_description__icontains=query)
        )
    else:
        recipes = Recipe.objects.all()
    
    context = {"Recipes": recipes}
    return render(request, 'display_all.html', context)

def recipe_detail(request, id):
    recipe = get_object_or_404(Recipe,id=id)

    return render(request,'recipe_detail.html',{'recipe':recipe})

@login_required
def recipe_update(request, id):
    recipe = Recipe.objects.get(id=id)

    if request.method == 'POST':
        recipe.recipe_name = request.POST.get('recipe_name')
        recipe.recipe_description = request.POST.get('recipe_description')

        recipe_image = request.FILES.get('recipe_image')
        if recipe_image:
            recipe.recipe_image = recipe_image

        recipe.save()
        messages.success(request, 'Recipe updated successfully!')
        return redirect('recipe_detail', id=recipe.id)

    return render(request, 'update_recipe.html', {'recipe': recipe})

@login_required
def recipe_delete(request, id):
    recipe = get_object_or_404(Recipe,id=id)
    recipe.delete()
    messages.success(request, 'Recipe deleted successfully!')
    return redirect('recipe_list')