# blogs/forms.py

from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'text']  # 只显示标题和内容字段


from django.contrib.auth.models import User

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']  # 你可以根据需求添加更多字段