from django.contrib import admin

from goods.models import Categories, Goods

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name',]


@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'price',]
    search_fields = ['name', 'description']
    list_filter = ['category',]
    fields = [
        'name',
        'category',
        'slug',
        'description',
        'image',
        'price',
        'power',
        'acceleration',
        'consumption',
        'emissions',
    ]
