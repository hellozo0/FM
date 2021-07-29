from django.contrib import admin
from .models import ComHospital
from .forms import PostForm

# Register your models here.
class ComHospitalAdmin(admin.ModelAdmin):
    list_display = ('title', 'writer', 'pub_date', 'update')
    readonly_fields = ['pub_date']
    form = PostForm

admin.site.register(ComHospital, ComHospitalAdmin)