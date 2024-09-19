from rest_framework import serializers
from .models import Author, BlogPost, Topic


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'age']


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id', 'title']


class BlogPostSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())
    topic = serializers.PrimaryKeyRelatedField(queryset=Topic.objects.all())

    class Meta:
        model = BlogPost
        fields = [
            'id',
            'title',
            'content',
            'publication_date',
            'author',
            'topic'
            ]

    def create(self, validated_data):
        # Extract the nested fields
        author = validated_data.pop('author')
        topic = validated_data.pop('topic')

        # Create the BlogPost instance
        blog_post = BlogPost.objects.create(
            author=author,
            topic=topic,
            **validated_data
            )
        return blog_post

    def update(self, instance, validated_data):
        # Update the author and topic fields
        instance.author = validated_data.get('author', instance.author)
        instance.topic = validated_data.get('topic', instance.topic)

        # Update the other fields
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.publication_date = validated_data.get(
            'publication_date',
            instance.publication_date
            )

        instance.save()
        return instance
