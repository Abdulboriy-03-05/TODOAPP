from django.urls import path
from .views import *
app_name = 'main'

urlpatterns = [
    path('',index,name="index"),
    path("delete/<int:todo_id>",deleteTodo, name="delete"),
    path("deleteall/",deleteAll,name="deleteall"),
    path("done/<int:todo_id>",done_todo,name="done"),
    path("update/<int:todo_id>",udpade,name="update"),
    path('updateall/<pk>',UpdateTodo.as_view(),name='updateall')
]