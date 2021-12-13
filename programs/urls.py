from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_programs, name='programs' ),
    path('<int:program_id>/', views.program_detail, name='program_detail'),
    path('add/', views.add_program, name='add_program'),
    path('edit/<int:program_id>/', views.edit_program, name='edit_program'),



]