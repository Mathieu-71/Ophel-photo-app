from django.urls import path
from . import views


urlpatterns = [
path('',views.home, name='home'),
path('/category', views.categoryPage, name='image-category'),
path('/category/<slug:slug1>', views.imageDetailPage, name='image-detail'),
]