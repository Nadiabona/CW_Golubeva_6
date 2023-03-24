from django.contrib import admin

from skymarket.ads.models import Ad, Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    comments_fields = ("pk", "author", "text")


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    admin_fields = ("pk", "author", "title", "price", "image")


