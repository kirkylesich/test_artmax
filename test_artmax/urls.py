from django.contrib import admin
from django.urls import path
from main.views import ProductSetView, ProductView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product_sets/', ProductSetView.as_view()),
    path('products/', ProductView.as_view())
]
