from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('branch/<int:pk>/', views.branch_detail, name='branch_detail')
]


