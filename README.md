# ToDo-Manager
MVP ToDo-Manager

## Description
API for creating and managing your notes, with the ability to assign completion status, priority, and category to each task.

## Getting Started

To create and edit tasks, you must [install project](https://github.com/KrohinV/ToDo-Manager) and log in or create an account by following the link:
[create](http://127.0.0.1:8000/api/v1/user/create),
[login](http://127.0.0.1:8000/api/v1/user/login/).

## Dependencies

* python 3.6
* Django 5.0
* Django REST framework 3.14.0
* Django Filter 23.5

## Installing

You can download the project [here](https://github.com/KrohinV/ToDo-Manager)

### Executing program

name of action| link
:-------------|:----
user|
create_user|http://127.0.0.1:8000/api/v1/user/create
get_users|http://127.0.0.1:8000/api/v1/api/v1/user/get_users
get_users_by_id|http://127.0.0.1:8000/api/v1/user/get/<int:id>
update_user|http://127.0.0.1:8000/api/v1/api/v1/user/update/<int:id>
delete_user|http://127.0.0.1:8000/api/v1/user/delete/<int:id>
task|
get_all_tasks|http://127.0.0.1:8000/api/v1/task/get_all
get_task_for_user|http://127.0.0.1:8000/api/v1/task/get_for_user/<int:id>
get_task_for_category|http://127.0.0.1:8000/api/v1/task/get_for_category/<int:id>
get_task_for_priority|http://127.0.0.1:8000/api/v1/task/get_for_priority/<int:id>
get_task_by_status|http://127.0.0.1:8000/api/v1/task/get_by_status/<str:status>
get_for_id|http://127.0.0.1:8000/api/v1/task/get/<int:id>
update_task|http://127.0.0.1:8000/update_task
delete_task|http://127.0.0.1:8000/delete_task
category|
create_category|http://127.0.0.1:8000/api/v1/category/create
get_category_by_id|http://127.0.0.1:8000/api/v1/category/get/<int:id>
update_category|http://127.0.0.1:8000/api/v1/category/update/<int:id>
delete_category|http://127.0.0.1:8000/api/v1/category/delete/<int:id>
priority|
create_priority|http://127.0.0.1:8000/api/v1/priority/create
get_priority_by_id|http://127.0.0.1:8000/api/v1/priority/get/<int:id>
update_priority|http://127.0.0.1:8000/api/v1/priority/update/<int:id>
delete_priority|http://127.0.0.1:8000/api/v1/priority/delete/<int:id>

