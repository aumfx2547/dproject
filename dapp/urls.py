from .views import *
from django.contrib import admin
from django.urls import path

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', index, name='index'),
    path('update/', update_content, name='update_content'),
    path('update2/', update_content2, name='update_content2'),
    path('add/', add_todo, name='add_todo'),
    path('delete/<int:todo_id>', delete_todo, name='delete_todo'),
	path('toggle/<int:todo_id>', toggle_todo, name='toggle_todo'),
    path('edit/<int:todo_id>', edit_todo, name='edit_todo'),
    path('edit_form/<int:todo_id>', edit_todo_form, name='edit_todo_form'),
    path('cancel/', cancel_edit, name='cancel_edit'),
]
