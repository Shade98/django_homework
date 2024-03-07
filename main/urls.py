from django.urls import path
from .views import *

urlpatterns = [
    path('categories/', get_categories),
    path('category-create/', create_category),
    path('category/<int:pk>/', get_category_by_id),
    path('category_update/<int:pk>',update_category),
    path('category_delete/<int:pk>',delete_category),

    path('tasks/',get_tasks),
    path('create_task/', create_task),
    path('task/<int:pk>',get_task_by_id),
    path('update_task/<int:pk>',update_task),
    path('delete_task/<int:pk>',delete_task)
] 