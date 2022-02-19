from django.contrib import admin

from backend.apps.products.models import Product, Category, SubCategory
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ("name", "id")


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ("name", "category","id")
    search_fields = ("name", "category__name")
    list_filter = ("category__name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "subcategory",
        "price",
        "is_active",
        "created",
    )
    search_fields = (
        "name",
        "price",
        "category__name",
        "subcategory_name"
    )
    list_filter = (
        "category__name",
        "subcategory__name",
        "is_active",
        "created",
    )
