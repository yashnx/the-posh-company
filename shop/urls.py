from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index , name="ShopHome"),
    path("about/", views.about , name="About"),
    path("contact/", views.contact , name="Contact"),
    path("search/", views.search , name="Search"),
    path("productview/", views.productview , name="Product View"),
    path("cart/", views.cart , name="cart"),
]