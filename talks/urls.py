from django.urls import path 
from . import views
 
urlpatterns = [
    path('',        views.talk_list, name='talk_list' ),
    path('create/', views.talk_create, name='talk_create' ),
    path('<int:talk_id>/edit/',    views.talk_edit, name='talk_edit' ),
    path('<int:talk_id>/delete/ ', views.talk_delete, name='talk_delete' ),
    path('register/ ', views.register, name='register' ),

]
