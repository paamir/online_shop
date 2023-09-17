from django.contrib import admin
from .models import Product, Comment


class CommentTabularInline(admin.StackedInline):
    model = Comment
    fields = ['user', 'text', 'is_active']
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'active', 'image']
    inlines = [CommentTabularInline]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return Comment.objects.all()
    list_display = ['product', 'creation_datetime', 'is_active']
