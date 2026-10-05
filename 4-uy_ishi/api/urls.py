from django.urls import path
from .views import (
    GenreListCreateView, GenreDetailView,
    BookListCreateView, BookDetailView,
    CommentListCreateView, CommentDetailView
)

urlpatterns = [
    path('genres/', GenreListCreateView.as_view()),
    path('genres/<int:id>/', GenreDetailView.as_view()),
    path('books/', BookListCreateView.as_view()),
    path('books/<int:id>/', BookDetailView.as_view()),
    path('comments/', CommentListCreateView.as_view()),
    path('comments/<int:id>/', CommentDetailView.as_view()),
]
