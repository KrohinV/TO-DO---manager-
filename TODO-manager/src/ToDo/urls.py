from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import urls
from task_manager.views import *

urlpatterns = [
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('admin/', admin.site.urls),
    path('api/v1/user/', include('rest_framework.urls')),

    # ___________USER______________
    # path('api/v1/user/create', create_user, name='create_user'),
    path('api/v1/user/create', CreateUser.as_view(), name='create_user'),
    # path('api/v1/user/get_all', get_all_users, name='get_users'),
    path('api/v1/user/get_users', GetAllUsers.as_view(), name='get_users'),
    path('api/v1/user/get/<int:id>', get_users_by_id, name='get_users_by_id'),
    # path('api/v1/user/update/<int:id>', update_user, name='update_user'),
    path('api/v1/user/update/<int:id>', UpdateUser.as_view(), name='update_user'),
    path('api/v1/user/delete/<int:id>', del_user, name='delete_user'),

    # ___________TASK______________
    # path('api/v1/task/create', create_task, name='create_task'),
    path('api/v1/task/create', CreateTask.as_view(), name='create_task'),
    # path('api/v1/task/get_all', get_all_tasks, name='get_all_tasks'),
    path('api/v1/task/get_all', TaskList.as_view(), name='get_all_tasks'),
    path('api/v1/task/get_for_user/<int:id>', get_task_for_user, name='get_task_for_user'),
    path('api/v1/task/get_for_category/<int:id>', get_task_for_category, name='get_task_for_category'),
    path('api/v1/task/get_for_priority/<int:id>', get_task_for_priority, name='get_task_for_priority'),
    path('api/v1/task/get/<int:id>', get_task_for_id, name='get_for_id'),
    path('api/v1/task/get_by_status/<str:status>', get_task_by_status, name='get_task_by_status'),
    # path('api/v1/task/update/<int:id>', update_task, name='update_task'),
    path('api/v1/task/update/<int:id>', UpdateTask.as_view(), name='update_task'),
    path('api/v1/task/delete/<int:id>', del_task, name='delete_task'),

    # ___________CATEGORY______________
    # path('api/v1/category/create', create_category, name='create_category'),
    path('api/v1/category/create', CreateCategory.as_view(), name='create_category'),
    path('api/v1/category/get/<int:id>', get_category_by_id, name='get_category_by_id'),
    # path('api/v1/category/update/<int:id>', update_category, name='update_category'),
    path('api/v1/category/update/<int:id>', UpdateCategory.as_view(), name='update_category'),
    path('api/v1/category/delete/<int:id>', del_category, name='delete_category'),

    # ___________PRIORITY______________
    # path('api/v1/priority/create', create_priority, name='create_priority'),
    path('api/v1/priority/create', CreatePriority.as_view(), name='create_priority'),
    path('api/v1/priority/get/<int:id>', get_priority_by_id, name='get_priority_by_id'),
    # path('api/v1/priority/update/<int:id>', update_priority, name='update_priority'),
    path('api/v1/priority/update/<int:id>', UpdatePriority.as_view(), name='update_priority'),
    path('api/v1/priority/delete/<int:id>', del_priority, name='delete_priority'),

]
