from django.contrib import admin
from django.urls import path
from main.views import ProductAndSetsListVIew

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products_and_sets/', ProductAndSetsListVIew.as_view())
]
