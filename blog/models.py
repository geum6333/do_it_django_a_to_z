from django.db import models
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField
from markdownx.utils import markdown
import os

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blog/category/{self.slug}/'

    class Meta:
        verbose_name_plural = 'Categories'

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blog/tag/{self.slug}/'

class Post(models.Model):
    title = models.CharField(max_length=50)  # 게시글 제목
    hook_text = models.CharField(max_length=100, blank=True)
    content = MarkdownxField()  # 게시글 본문 내용
    
    created_at = models.DateTimeField(auto_now_add=True)  # 게시글 게시 날짜
    updated_at = models.DateTimeField(auto_now=True)

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)

    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)

    tags = models.ManyToManyField(Tag, blank=True)

    # 포스트 제목
    def __str__(self):
        return f'[{self.pk}]{self.title} :: {self.author}'
    def get_absolute_url(self):
        return f'/blog/{self.pk}/'
    def get_file_name(self):
        return os.path.basename(self.file_upload.name)
    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]
    def get_content_markdown(self):
        return markdown(self.content)
# Create your models here.

