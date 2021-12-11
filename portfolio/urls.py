from django.urls import path
from . import views

urlpatterns = [
    path('portfolios', views.portfolio_list, name='portfolio_list'),
    path('portfolios/<int:pk>/', views.portfolio_detail, name='portfolio_detail'),
    path('portfolios/new', views.portfolio_new, name='portfolio_new'),
    path('portfolios/<int:pk>/edit/', views.portfolio_edit, name='portfolio_edit'),
]