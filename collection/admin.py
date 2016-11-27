from django.contrib import admin
from django.contrib.sites.requests import RequestSite
from collection.models import Post


# Register your models here.

class PostAdmin(admin.ModelAdmin):
	model = Post
	list_display = ('title', 'content',)
	prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)