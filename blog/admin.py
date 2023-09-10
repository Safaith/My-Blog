from django.contrib import admin

# Register your models here.
from .models import Post, Author, Tag,comment


class postAdmin(admin.ModelAdmin):
    list_filter = ("author", "tags", "date",)
    list_display = ("title", "date", "author",)
    prepopulated_fields = {"slug": ("title",)}

class commentAdmin(admin.ModelAdmin):
    list_display= ("user_name","post")


admin.site.register(Post, postAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(comment,commentAdmin)