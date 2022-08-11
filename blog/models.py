from django.db import models
import os

class Post(models.Model):
    title = models.CharField(max_length=50)  # 게시글 제목
    hook_text = models.CharField(max_length=100, blank=True)
    content = models.TextField()  # 게시글 본문 내용
    
    created_at = models.DateTimeField(auto_now_add=True)  # 게시글 게시 날짜
    updated_at = models.DateTimeField(auto_now=True)

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)

    # auther: 추후 작성 예정
    def __str__(self):
        return f'[{self.pk}]{self.title}'
    def get_absolute_url(self):
        return f'/blog/{self.pk}'
    def get_file_name(self):
        return os.path.basename(self.file_upload.name)
    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]
# Create your models here.

