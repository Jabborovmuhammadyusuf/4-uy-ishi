from rest_framework import serializers
from .models import Genre, Book, Comment

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    genre_id = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all(), source='genre', write_only=True)
    class Meta:
        model = Book
        exclude = ['description']
        depth = 1
        extra_kwargs = {
            'price': {'required': True}
        }

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['user', 'created_at']
