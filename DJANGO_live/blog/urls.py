from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.post_list, name='all_posts'),
    path('create/', views.post_create, name='create_post'),
    path('delete/<int:pk>/', views.post_delete, name='delete'),
    path('post/<int:pk>/', views.post_page, name='post_page'),
    path('edit/<int:pk>/', views.edit_post, name='edit_page'),
]

