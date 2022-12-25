from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    # we are populating slug from title
    prepopulated_fields = {'slug': ('title',)}
    # filter post by their status or by the created date
    list_filter = ('status', 'created_on')
    # to control which fields are displayed on the change list page of the
    # admin
    list_display = ('title', 'slug', 'status', 'created_on')
    # to search on title and content
    search_fields = ['title', 'content']
    summernote_fields = ('contents')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)

