from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.create, name='create'),
    path('get/', views.read_all, name='read_all'),
    path('get/<id>', views.read, name='read'),
    path('put/<id>', views.update, name='update'),
    path('delete/<id>', views.delete, name='delete')
]