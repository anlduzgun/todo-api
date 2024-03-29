from django.urls import path
from .views import todo_delete, todo_delete_all, todo_list, todo_post, todo_update_done, todo_update_description

urlpatterns = [
    #path('signup/', signup, name='signup'),
    #path('login/', login, name='login'),
    path('todos/get/', todo_list, name = 'todo_list' ),
    path('todos/delete/<int:todo_id>/', todo_delete, name = 'todo_delete' ),
    path('todos/post/', todo_post, name = 'todo_post' ),
    path('todos/update/done/<int:todo_id>/', todo_update_done, name = 'todo_update_done'),
    path('todos/update/description/<int:todo_id>/', todo_update_description, name = 'todo_update_description'),
    path('todos/delete/all', todo_delete_all, name = 'todo_delete_all' ),
]
