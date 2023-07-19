from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('confirm', views.confirmDelete, name='confirm'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('details/<int:id>', views.details, name='details'),
    path('delete/<int:id>', views.deleteStudent, name='delete'),
    # path('signin', views.signin, name='signin')
    
]
