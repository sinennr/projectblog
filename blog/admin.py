from webbrowser import register

from django.contrib import admin
from django.contrib.auth.models import Permission

from .models import Comment, Post, User

# Register your models here.
admin.site.register(Permission)

class User_Admin(admin.ModelAdmin):
    list_display = ['username','first_name','last_name','email']

class PostAdmin(admin.ModelAdmin):
    list_display = ['title','user','create_time','update_time']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['post','user','create_time']

admin.site.register(User, User_Admin)

admin.site.register(Post, PostAdmin)

admin.site.register(Comment, CommentAdmin)
