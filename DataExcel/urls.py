from django.urls import path
from . import views

urlpatterns = [
    path('', views.excel_data_table, name='excel_data_table'),               # List view with search
    path('<int:pk>/', views.excel_data_detail, name='excel_data_detail'),    # Detail view
    path('create/', views.excel_data_create, name='excel_data_create'),      # Create view
    path('<int:pk>/edit/', views.excel_data_update, name='excel_data_update'),  # Update view
    path('<int:pk>/delete/', views.excel_data_delete, name='excel_data_delete'),  # Delete confirmation view
]
