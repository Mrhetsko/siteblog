from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('category/<str:slug>/', views.get_category, name='category'),
]
