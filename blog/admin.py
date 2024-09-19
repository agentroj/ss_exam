from django.contrib import admin
from .models import BlogPost, Author, Topic

admin.site.register(BlogPost)
admin.site.register(Author)
admin.site.register(Topic)
