from django.urls import path
from . import views

urlpatterns = [

    path('signup', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('', views.home, name='home'),
    path('todolist', views.ToDolist, name='todolist'),
    path('contact', views.contact, name='contact'),
    path('viewtask', views.viewtask, name='viewtask'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
]


