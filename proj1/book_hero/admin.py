from django.contrib import admin
from book_hero.models import *


# 关联注册（stack类型）
# class HeroInfoInline(admin.StackedInline):
#     model = HeroInfo
#     extra = 2


# 关联注册（表格类型）
class HeroInfoInline(admin.TabularInline):
    model = HeroInfo
    extra = 2


# 自定义管理界面
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ["id", "btitle", "bpub_date"]
    list_filter = ["btitle"]
    search_fields = ["btitle"]
    list_per_page = 10
    fieldsets = [
        ("basic", {"fields": ["btitle"]}),
        ("more", {"fields": ["bpub_date"]}),
    ]
    inlines = [HeroInfoInline]


# 注册模型
admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo)
