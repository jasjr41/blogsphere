from django.contrib import admin
from .models import Post, Author,Tag

class PostAdmin(admin.ModelAdmin):
    list_filter = ('title','author')
    list_display = ['title','author']

# Register your models here.
admin.site.register(Post,PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
