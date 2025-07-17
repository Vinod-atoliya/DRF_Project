from rest_framework import serializers
from .models import Blog ,Comment

class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class Blogserializers(serializers.ModelSerializer):
    comments = CommentSerializers(many= True, read_only= True)
    class Meta:
        model = Blog
        fields = '__all__'
        