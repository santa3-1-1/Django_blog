# blogs/admin.py

from django.contrib import admin
from .models import BlogPost

admin.site.register(BlogPost)  # 注册 BlogPost 模型
