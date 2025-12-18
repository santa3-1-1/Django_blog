from django.db import models
# blogs/models.py
from django.contrib.auth.models import User  # 导入 User 模型
from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=200)  # 博客标题
    text = models.TextField()  # 博客内容
    date_added = models.DateTimeField(auto_now_add=True)  # 创建时间，自动填充
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # 1 是默认用户 ID
    def __str__(self):
        return self.title  # 在 admin 中显示标题

# Create your models here.
