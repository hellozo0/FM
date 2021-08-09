from django.db import models
from django.conf import settings
from django.forms.fields import BooleanField
from django.contrib.auth.models import AbstractUser

#커뮤니티 table 형식 만들기 (사진, 제목, 본문)
class Community(models.Model):
    writer = models.ForeignKey('account.CustomUser', related_name='articles', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200, verbose_name="제목")
    body = models.TextField(verbose_name="내용")
    pub_date = models.DateTimeField(auto_now_add=True, null=True, verbose_name="작성일")
    update = models.DateTimeField(auto_now=True, null=True, verbose_name="최종수정일")

    def __str__(self):
        return self.title

#증상검색 checkbox
class Symptom:
    published = BooleanField()