from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='todo-index'),
    path('add/', views.addTodo, name='add'),
    path('complete/<todo_id>/', views.completeTodo, name='complete'),
    path('deletecomplete/', views.deleteComplete, name='deletecomplete'),
    path('deleteall/', views.deleteAll, name='deleteall'),
]
