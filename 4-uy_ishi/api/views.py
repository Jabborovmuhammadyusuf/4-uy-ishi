from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from .models import Genre, Book, Comment
from .serializers import GenreSerializer, BookSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly

class GenreListCreateView(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions]
    def get_queryset(self):
        return Genre.objects.all()
    def get_serializer_class(self):
        return GenreSerializer

class GenreDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [DjangoModelPermissions]
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

class BookListCreateView(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions]
    def get_queryset(self):
        return Book.objects.all()
    def get_serializer_class(self):
        return BookSerializer

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [DjangoModelPermissions]
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    lookup_field = 'id'
    lookup_url_kwarg = 'id'
