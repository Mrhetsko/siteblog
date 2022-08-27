from django.urls import path
from . import views


urlpatterns = [
    # path('', views.index, name='home'),
    path('', views.Home.as_view(), name='home'),
    path('category/<str:slug>/', views.get_category, name='category'),
    path('post/<str:slug>/', views.get_post, name="post")
]
