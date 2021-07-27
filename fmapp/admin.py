from django.contrib import admin
from .models import Community
# Register your models here.
class CommunityAdmin(admin.ModelAdmin):
    list_display = ('title', 'writer', 'pub_date', 'update')
admin.site.register(Community, CommunityAdmin)