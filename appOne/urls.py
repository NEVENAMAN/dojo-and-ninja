from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('register_dojo',views.registerDojo),
    path('register_ninja',views.redisterNinja),
    path('get_all',views.get_dojo),
    path('delete/<int:id>',views.delete,name='delete')
]