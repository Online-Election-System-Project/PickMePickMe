from django.urls import path
from . import views

urlpatterns = [
    path('promotions', views.promotion_list, name='promotion_list'),
    path('promotions/<int:pk>/', views.promotion_detail, name='promotion_detail'),
    path('promotions/new', views.promotion_new, name='promotion_new'),
    path('promotions/<int:pk>/edit/', views.promotion_edit, name='promotion_edit'),
]