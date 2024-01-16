from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('shop', views.shop, name="shop"),
    path('contact', views.contact, name="contact"),
    path('details/<str:id>', views.bookDetails, name="bookDetails"),
    path("category/<str:name>", views.category, name="category"),
    path('search', views.search, name="search"),
    path('register/', views.register, name="register"),
    path('cart', views.cart, name="cart"),
    path('checkout', views.checkout, name="checkout"),
    path('news', views.news, name="news"),
    path('newsDetails/<str:title>', views.newsDetails, name="newsDetails"),
    path('compare', views.compare, name="compare"),
    path('wishlist', views.wishlist, name="wishlist"),
    path('account', views.account, name="account"),
    path('order_complete', views.order_complete, name="order_complete"),
    path('faq', views.faq, name="faq"),



    # path("post/<str:id>", views.post, name="post"),
]
