"""fmproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from fmapp.views import home
import fmapp.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('fmapp/', include('fmapp.urls')),
    path('account/', include('account.urls')), #계정 만드는 앱에 따로 urls.py만들었을 경우
    path('fmapp/<int:community_id>', fmapp.views.write, name="write"),
    path('fmapp/new', fmapp.views.new, name='new'),
    path('fmapp/postcreate', fmapp.views.postcreate, name='postcreate'),
    path('fmapp/edit', fmapp.views.edit, name='edit'),
    path('fmapp/postupdate/<int:community_id>', fmapp.views.postupdate, name='postupdate'),
    path('fmapp/postdelete/<int:community_id>', fmapp.views.postdelete, name='postdelete'),
] #+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) #커뮤니티에서 사진 받는 경우 해당 static추가...?!
#static을 병렬적으로 더해주는 형태
