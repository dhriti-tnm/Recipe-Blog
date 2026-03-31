"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from vegies.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('recipe/create/', recipes, name='add_recipe'),
    path('', all_recipes, name='recipe_list'),
    path('recipe/<int:id>/', recipe_detail, name='recipe_detail'),
    path('recipe/update/<int:id>/', recipe_update, name='recipe_update'),
    path('recipe/delete/<int:id>/', recipe_delete, name='recipe_delete'),
    
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()