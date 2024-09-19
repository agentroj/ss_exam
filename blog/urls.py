from django.urls import path
from . import views

urlpatterns = [
    # Author CRUD
    path(
        'authors/', views.AuthorListCreateAPIView.as_view(),
        name='author_list_create'),
    path(
        'authors/<int:pk>/', views.AuthorDetailAPIView.as_view(),
        name='author_detail'),

    # BlogPost API endpoints
    path(
        'blogposts/', views.BlogPostListCreateAPIView.as_view(),
        name='blogpost_list_create'),
    path(
        'blogposts/<int:pk>/', views.BlogPostDetailAPIView.as_view(),
        name='blogpost_detail'),

    # Topic API endpoints
    path(
        'topics/', views.TopicListCreateAPIView.as_view(),
        name='topic_list_create'),
    path(
        'topics/<int:pk>/', views.TopicDetailAPIView.as_view(),
        name='topic_detail'),
]
