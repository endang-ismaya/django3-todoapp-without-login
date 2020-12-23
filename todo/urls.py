from django.urls import path
from todo.views import todo_list, todo_detail, todo_create, todo_update, todo_delete

app_name = 'todo'

urlpatterns = [
    path('', todo_list, name='todo_list'),
    path('create/', todo_create, name='todo_create'),
    path('<int:todo_id>/', todo_detail, name='todo_detail'),
    path('<int:todo_id>/update/', todo_update, name='todo_update'),
    path('<int:todo_id>/delete/', todo_delete, name='todo_delete'),
]
