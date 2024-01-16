from django.urls import path, include
from . import views

app_name = 'basket'

urlpatterns = [
    path('basket/', include([
        # path('', views.basket_list, name='list'),
        path('<bookTitle>/add/', views.add_to_basket, name='add'),
        path('<bookTitle>/remove/', views.remove_from_basket, name='remove'),
        path('delete/', views.delete_basket, name='delete'),
    ])),
]
