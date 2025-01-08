from django.urls import path
from .views import index,list,create,update,delete

urlpatterns = [
    path('',index,name='index'),
    path('list/',list,name='list'),
    path('create/',create,name='create'),
    path('update/<int:pk>/',update,name='update'),
    path('delete/<int:pk>/',delete,name='delete'),
]