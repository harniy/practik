from django.contrib import admin

# Register your models here.
from .models import Main, Category, SubCategory, Profile, Comment, FeedBack


@admin.register(Main)
class MainAdmin(admin.ModelAdmin):
    list_display = ('name', 'date',)
    list_display_links = ('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "avatar",)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "user", "reply", "content",)

@admin.register(FeedBack)
class FeedBackAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'description','time',)
    list_display_links = ('name',)