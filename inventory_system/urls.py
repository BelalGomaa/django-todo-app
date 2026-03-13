from django.contrib import admin
from django.urls import path
from stock.views import product_list
from todo.views import task_list, delete_task, toggle_task

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', product_list, name='product_list'),
    path('todo/', task_list, name='task_list'),
    path('todo/delete/<int:pk>/', delete_task, name='delete_task'),
    path('todo/toggle/<int:pk>/', toggle_task, name='toggle_task'),
]