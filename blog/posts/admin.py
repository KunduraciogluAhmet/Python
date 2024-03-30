from django.contrib import admin
from .models import Post
# Register your models here.
#admin.site.register(Post)


class PostAdmin(admin.ModelAdmin):
    list_display = ['title','date']
    search_fields = ['title','content']
    list_display_links =['title','date']
    list_filter = ['date']

admin.site.register(Post,PostAdmin)

