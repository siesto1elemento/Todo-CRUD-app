from django.urls import path
from . import views
from .views import Addtodo,Updatetodo,Deletetodo

urlpatterns = [
    path('',views.home, name="home"),
    path('todo/',Addtodo.as_view(),name='add_todo'),
    path('todo/<int:pk>',Updatetodo.as_view(),name='update_todo'),
    path('todo/delete/<int:pk>',Deletetodo.as_view(),name='delete_todo'),

]