from django.urls import path
from . import views
urlpatterns = [
    path('', views.root),
    path('blogs/', views.index),
    path('blogs/new/', views.new),
    path('blogs/create/', views.create),
    path('blogs/<_numero>/<int:_nn>', views.show),
    path('blogs/<_numero>/edit', views.edit),
    path('blogs/<_numero>/delete', views.delete),

]
