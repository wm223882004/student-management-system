from django.urls import path
from . import views

urlpatterns = [
    path('', views.grade_list, name='grade_list'),
    path('add/', views.grade_add, name='grade_add'),
    path('edit/<int:pk>/', views.grade_edit, name='grade_edit'),
    path('delete/<int:pk>/', views.grade_delete, name='grade_delete'),
    path('statistics/', views.grade_statistics, name='grade_statistics'),
]
