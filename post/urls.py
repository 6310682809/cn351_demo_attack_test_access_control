from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:post_id>', views.view_post, name='view_post'),
    path('post/create/', views.create_post, name='create_post'),
    path('post/edit/<int:post_id>', views.edit_post, name='edit_post'),
    path('post/delete/<int:post_id>', views.delete_post, name='delete_post'),
]