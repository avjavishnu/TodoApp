from .views import add_task, done, add, get_tasks, recordupdate,update, delete_task, pending_tasks, completed_tasks, index_view
from django.urls import path

urlpatterns = [
    path("addtask", add_task, name='addtask'),
    path("added", done, name='added'),
    path("add", add, name='add'),
    path("display", get_tasks, name="display"),
    path('update/recordupdate/<int:idn>', recordupdate, name='recordupdate'),
    path('update/<int:idn>', update, name="update"),
    path('delete/<int:idn>', delete_task, name="delete"),
    path('pending', pending_tasks, name="pending"),
    path('completed', completed_tasks, name='completed'),
    path('index', index_view, name='index')
]
