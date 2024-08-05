from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.create_post, name='create_post'),
    path("", views.post_list, name='post_list'),
    path('register/', views.register, name='register'),
    path("<slug:slug>/", views.post_detail, name='post_detail'),
    path("<slug:slug>/like/", views.like, name='like'),
    path("<slug:slug>/dislike", views.dislike, name='dislike'),
    path('<slug:slug>/delete/', views.delete_post, name='delete_post'),
    path('<slug:slug>/<str:hashtag>/', views.post_list, name='post_list'),
]