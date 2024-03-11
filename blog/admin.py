from django.contrib import admin
from .models import Post, Contact, Comment, Category


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'image', 'is_published', 'view_count', 'created_at')
    list_display_links = ('id', 'author', 'image')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email', 'subject', 'is_solved', 'created_at')
    list_display_links = ('id', 'full_name', 'email')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'message', 'is_published', 'created_at')
    list_display_links = ('id', 'name', 'email',)


admin.site.register(Post, PostAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category)


