from django.urls import path
from . import views

urlpatterns=[
path("",views.list,name='list'),
path('add',views.add,name='new_add'),
path('edit/<int:id>',views.edit,name='edit_book'),
path('update/<int:id>',views.update,name='update_book'),
path('delete/<int:id>',views.delete,name='delete_book')
]