from django.contrib import admin
from .models import Qna
from .forms import PostForm

# Register your models here.
class QnaAdmin(admin.ModelAdmin):
    list_display = ('title', 'writer', 'pub_date', 'update')
    readonly_fields = ['pub_date']
    form = PostForm

admin.site.register(Qna, QnaAdmin)