from django.contrib import admin
from .models import BlogArticles

# Register your models here.

class BlogArticlesAdmin(admin.ModelAdmin):
    '''设置列表可显示的字段'''
    list_display = ("title","author","publish")
    '''设置过滤选项'''
    list_filter = ("publish","author")
    '''每页显示条目数'''
    list_per_page = 5

    '''设置可编辑字段'''
    #list_editable = ('title',)

    '''另外两个常用选项是 list_display_links和search_fields。前者设置带链接的字段，比如本例中带链接的字段为('title'), 
    后者设置可以搜索的字段，如('title', 'body')，方便快速查询需要修改的数据表条目。'''
    search_fields = ('title','body')

    '''单对多关系的选择之raw_id_fields选项 '''
    raw_id_fields = ("author",)

    '''按日期月份筛选'''
    date_hierarchy = "publish"

    '''按发布日期和作者排序'''
    ordering = ["publish","author"]

admin.site.register(BlogArticles,BlogArticlesAdmin)


