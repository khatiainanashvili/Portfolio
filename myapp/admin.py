from django.contrib import admin # type: ignore
from .models import  User, Tools, Illustration, Collections, Comment
# Register your models here.


admin.site.register(User)
admin.site.register(Tools)
admin.site.register(Illustration)
admin.site.register(Comment)

class CollectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_favorite')
    list_filter = ('is_favorite', )

admin.site.register(Collections, CollectionAdmin)