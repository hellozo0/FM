from django.contrib import admin
from .models import Community, ComHospital, Qna
from .forms import PostForm, PostFormm, PostFormmm
# Register your models here.
class CommunityAdmin(admin.ModelAdmin):
    list_display = ('title', 'writer', 'pub_date', 'update')
    readonly_fields = ['pub_date']
    form = PostForm
class ComHospitalAdmin(admin.ModelAdmin):
    list_display = ('title', 'writer', 'pub_date', 'update')
    readonly_fields = ['pub_date']
    form = PostFormm
class QnaAdmin(admin.ModelAdmin):
    list_display = ('title', 'writer', 'pub_date', 'update')
    readonly_fields = ['pub_date']
    form = PostFormmm
admin.site.register(Community, CommunityAdmin)
admin.site.register(ComHospital, ComHospitalAdmin)
admin.site.register(Qna, QnaAdmin)