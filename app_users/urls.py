from django.urls import path

from . import views

urlpatterns = [
    path('', views.login_user, name='login'),
    path('registration/', views.user_registration, name='registration'),

    path('notes/', views.notes_list, name='notes_list'),
    path('note/<uuid:note_id>/', views.note_detail, name='note_detail'),
    path('note/create/', views.note_create, name='note_create'),
    path('note/update/<uuid:note_id>/', views.note_update, name='note_update'),
    path('note/delete/<uuid:note_id>/', views.note_delete, name='note_delete'),
]
