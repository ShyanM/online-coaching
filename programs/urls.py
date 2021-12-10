from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_programs, name='programs' ),
    path('<program_id>', views.program_detail, name='program_detail'),

]