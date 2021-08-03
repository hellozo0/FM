from django.contrib import admin
from .models import Community
from .forms import PostForm
# Register your models here.
class CommunityAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'update', 'writer')
    readonly_fields = ['pub_date']
    form = PostForm

admin.site.register(Community, CommunityAdmin)
