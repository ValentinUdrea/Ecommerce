# This file is in charge of connecting the views to urls

from django.urls import path
from . import views
# . represents the folder you are in

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('products/', views.getProducts, name="products"),
    path('products/<str:pk>/', views.getProduct, name="product"),

]