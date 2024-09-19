from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Topic(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    publication_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
