from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ComHospital(models.Model):
    title = models.CharField(max_length=200, verbose_name="제목")
    body = models.TextField(verbose_name="내용")
    writer = models.CharField(max_length=200, verbose_name="작성자")
    #writer 부분은 수정 필요 (아이디를 가져와야 하므로)
    pub_date = models.DateTimeField(auto_now_add=True, null=True, verbose_name="작성일")
    update = models.DateTimeField(auto_now=True, null=True, verbose_name="최종수정일")

    def __str__(self):
        return self.title