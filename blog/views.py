from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from .models import Author, BlogPost, Topic
from .serializers import AuthorSerializer, BlogPostSerializer, TopicSerializer


# Author Views
class AuthorListCreateAPIView(APIView):
    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorDetailAPIView(APIView):
    def get(self, request, pk):
        author = get_object_or_404(Author, pk=pk)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)

    def put(self, request, pk):
        author = get_object_or_404(Author, pk=pk)
        serializer = AuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        author = get_object_or_404(Author, pk=pk)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# BlogPost Views
class BlogPostListCreateAPIView(APIView):
    def get(self, request):
        blog_posts = BlogPost.objects.all()
        serializer = BlogPostSerializer(blog_posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BlogPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogPostDetailAPIView(APIView):
    def get(self, request, pk):
        blog_post = get_object_or_404(BlogPost, pk=pk)
        serializer = BlogPostSerializer(blog_post)
        return Response(serializer.data)

    def put(self, request, pk):
        blog_post = get_object_or_404(BlogPost, pk=pk)
        serializer = BlogPostSerializer(blog_post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        blog_post = get_object_or_404(BlogPost, pk=pk)
        blog_post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Topic Views
class TopicListCreateAPIView(APIView):
    def get(self, request):
        topics = Topic.objects.all()
        serializer = TopicSerializer(topics, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TopicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TopicDetailAPIView(APIView):
    def get(self, request, pk):
        topic = get_object_or_404(Topic, pk=pk)
        serializer = TopicSerializer(topic)
        return Response(serializer.data)

    def put(self, request, pk):
        topic = get_object_or_404(Topic, pk=pk)
        serializer = TopicSerializer(topic, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        topic = get_object_or_404(Topic, pk=pk)
        topic.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
