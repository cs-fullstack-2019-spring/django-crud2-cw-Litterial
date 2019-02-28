from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),  #List of all names
    path('create/',views.createUser,name="create"),  #creates a new user
    path('edit/<int:ID>/',views.editUser,name="edit"),  #edits a user
    path('delete/<int:ID>/',views.deleteUser,name="delete"),  #deletes a user
    path('read/<int:ID>/',views.readUser,name='read'),   #gets info of a user

]