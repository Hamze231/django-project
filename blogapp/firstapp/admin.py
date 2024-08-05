from django.contrib import admin

from firstapp.models import Comments, Post, Profile, Subscribe, Tag, WebsiteMeta

# Register your models here.
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Comments)
admin.site.register(Subscribe)
admin.site.register(Profile)
admin.site.register(WebsiteMeta)

