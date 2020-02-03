from django.contrib import admin
from TestModel.models import Test, Contact, Tag


# Register your models here.
# 内联(从属关系)显示
class TagInline(admin.TabularInline):
    model = Tag


# 创建自定义表单（admin界面只显示部分修改项）
# 1.初级的方式
# class ContactAdmin(admin.ModelAdmin):
#     fields = ("name", "email")
# 2.高级的方式
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'email')
    search_fields = ('name', )
    inlines = [TagInline]
    fieldsets = (
        ['Main', {
            'fields': ('name', 'email'),
        }],
        ['Advance', {
            'classes': ('collapse', ),
            'fields': ('age', ),
        }]
    )


admin.site.register(Contact, ContactAdmin)
admin.site.register([Test])
