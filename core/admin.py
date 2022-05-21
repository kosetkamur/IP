from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from simple_history.admin import SimpleHistoryAdmin

from .models import *


class PostResource(resources.ModelResource):
    class Meta:
        model = Post
        field = (
            "title",
            "time_to_cook",
            "count",
            "body",
            "slug",
            "cat",
            "dish",
        )

    def dehydrate_cat(self, post):
        post_cat = getattr(post.cat, "category", "unknown")
        return post_cat

    def dehydrate_dish(self, post):
        post_dish = getattr(post.dish, "viewDish", "unknown")
        return post_dish


class PostAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    resource_class = PostResource
    list_display = ('id', 'title', 'time_to_cook', 'count', )
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')


class PostHistoryAdmin(SimpleHistoryAdmin):
    pass


admin.site.register(Post, PostAdmin)
# admin.site.register(Post, PostHistoryAdmin)

