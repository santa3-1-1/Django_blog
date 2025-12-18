# Django博客系统

一个功能完整的个人博客平台，基于Django框架开发，支持用户注册、登录、发布和管理博客文章。

## 📋 功能特性

### 🎯 核心功能
- ✅ **用户认证系统**：注册、登录、登出功能
- ✅ **博客文章管理**：创建、编辑、删除博客文章
- ✅ **个人中心**：查看和编辑个人资料
- ✅ **权限控制**：用户只能管理自己的文章
- ✅ **响应式设计**：适配桌面、平板和手机设备

### 🔐 安全特性
- 🔒 多层权限验证（视图层、模板层、数据层）
- 🔐 防止跨站请求伪造（CSRF）保护
- 🔐 用户密码加密存储
- 🔐 防越权操作验证
- 🔐 安全的会话管理

### 🎨 用户体验
- 📱 响应式布局，支持移动端
- ✨ 现代化的界面设计
- 💬 操作结果即时反馈
- 📄 文章分页浏览
- 🎯 直观的操作流程

## 🏗️ 系统架构

### 技术栈
- **后端框架**：Django 4.2.8
- **前端技术**：HTML5 + CSS3 + Bootstrap 5
- **数据库**：SQLite3（开发）/ PostgreSQL（生产）
- **开发语言**：Python 3.9+
- **模板引擎**：Django模板语言

### 项目结构
```
blog_project/
├── blogs/                          # 核心应用
│   ├── migrations/                 # 数据库迁移文件
│   ├── static/blogs/css/          # 模块化CSS系统
│   │   ├── styles.css            # 全局基础样式
│   │   ├── home.css              # 首页专用样式
│   │   ├── edit_blog_post.css    # 文章编辑样式
│   │   ├── profile.css           # 个人中心样式
│   │   └── login.css             # 登录样式
│   ├── templates/                 # 模板系统
│   │   ├── blogs/                # 博客页面模板
│   │   └── registration/         # 认证页面模板
│   ├── models.py                 # 数据模型
│   ├── views.py                  # 视图逻辑
│   ├── forms.py                  # 表单定义
│   ├── urls.py                   # URL路由
│   └── admin.py                  # 后台管理
├── blog_project/                  # 项目配置
├── db.sqlite3                    # 数据库文件
└── manage.py                     # 管理脚本
```

## 🚀 快速开始

### 环境要求
- Python 3.8 或更高版本
- pip 包管理工具

### 安装步骤

1. **克隆项目**
```bash
git clone https://github.com/santa3-1-1/Django_blog.git
cd Django_blog
```

2. **创建虚拟环境**（推荐）
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. **安装依赖**
```bash
pip install -r requirements.txt
```

4. **数据库迁移**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **创建超级用户**（可选，用于后台管理）
```bash
python manage.py createsuperuser
```

6. **运行开发服务器**
```bash
python manage.py runserver
```

7. **访问应用**
- 博客首页：http://127.0.0.1:8000
- 管理后台：http://127.0.0.1:8000/admin

## 📖 使用指南

### 普通用户
1. **注册账号**：点击导航栏"注册"按钮，填写用户名、邮箱和密码
2. **登录系统**：使用注册的账号登录
3. **发布文章**：登录后点击"写文章"，填写标题和内容
4. **管理文章**：在个人中心查看和管理自己的文章
5. **编辑资料**：在个人中心修改用户名和邮箱

### 管理员
1. 访问管理后台：http://127.0.0.1:8000/admin
2. 使用超级用户账号登录
3. 可以管理所有用户和文章

## 🔧 项目配置

### 数据库配置
默认使用SQLite，如需更换数据库：

```python
# blog_project/settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'blog_db',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 静态文件配置
```python
# 开发环境
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# 生产环境
STATIC_ROOT = BASE_DIR / 'staticfiles'
```

## 📱 功能演示

### 博客首页
- 展示所有用户发布的文章
- 按发布时间倒序排列
- 每页显示5篇文章
- 支持分页浏览

### 文章详情
- 查看文章完整内容
- 显示作者和发布时间
- 作者可编辑或删除文章

### 个人中心
- 查看个人信息
- 管理自己发布的文章
- 编辑个人资料

## 🔍 权限控制流程

系统采用三层权限验证机制：

1. **视图层验证**：`@login_required`装饰器确保用户登录
2. **数据层验证**：检查当前用户是否为资源所有者
3. **模板层验证**：在界面中动态显示操作按钮

```python
# 编辑文章的权限验证示例
@login_required
def edit_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    
    # 验证用户是否为文章作者
    if post.user != request.user:
        messages.error(request, '您只能编辑自己发布的文章')
        return redirect('home')
    
    # 处理编辑逻辑...
```

## 🧪 运行测试

运行Django测试套件：

```bash
# 运行所有测试
python manage.py test

# 运行特定应用的测试
python manage.py test blogs

# 运行测试并显示详细信息
python manage.py test --verbosity=2
```

## 📁 核心代码结构

### 数据模型 (models.py)
```python
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
```

### 视图逻辑 (views.py)
```python
# 主要视图函数
- home()        # 博客首页
- new_post()    # 创建文章
- edit_post()   # 编辑文章
- delete_post() # 删除文章
- profile()     # 个人中心
- signup()      # 用户注册
- CustomLoginView() # 自定义登录视图
```

### 表单定义 (forms.py)
```python
# 主要表单类
- BlogPostForm         # 博客文章表单
- CustomUserCreationForm # 用户注册表单
- UserProfileForm      # 用户资料表单
```

## 🌐 API接口

### RESTful API端点
```
GET    /                    # 获取所有文章
POST   /new/               # 创建新文章
GET    /edit/<int:pk>/     # 获取文章编辑表单
POST   /edit/<int:pk>/     # 更新文章
POST   /delete/<int:pk>/   # 删除文章
GET    /profile/           # 获取用户资料
POST   /profile/edit/      # 更新用户资料
POST   /signup/            # 用户注册
POST   /accounts/login/    # 用户登录
POST   /accounts/logout/   # 用户登出
```

## 🐛 故障排除

### 常见问题

1. **数据库迁移失败**
```bash
# 删除数据库并重新迁移
rm db.sqlite3
python manage.py migrate
```

2. **静态文件未加载**
```bash
# 收集静态文件
python manage.py collectstatic
```

3. **端口被占用**
```bash
# 指定其他端口
python manage.py runserver 8001
```

4. **导入错误**
```bash
# 重新安装依赖
pip install --upgrade -r requirements.txt
```

### 调试模式
```python
# settings.py
DEBUG = True  # 开发环境设为True
DEBUG = False # 生产环境设为False
```

## 🔄 部署指南

### 本地部署
1. 确保已安装Python和Django
2. 按照"快速开始"步骤配置
3. 运行开发服务器

### 生产环境部署建议
1. 使用PostgreSQL替代SQLite
2. 配置Nginx + Gunicorn
3. 设置DEBUG=False
4. 配置ALLOWED_HOSTS
5. 启用HTTPS
6. 设置安全密钥
7. 配置静态文件和媒体文件

## 🤝 贡献指南

欢迎提交Issue和Pull Request！

1. Fork 本仓库
2. 创建功能分支：`git checkout -b feature/your-feature`
3. 提交更改：`git commit -m 'Add some feature'`
4. 推送分支：`git push origin feature/your-feature`
5. 提交Pull Request

### 开发规范
- 遵循PEP 8 Python代码规范
- 添加适当的注释
- 更新相关文档
- 编写单元测试

## 📄 开源协议

本项目采用MIT协议。详见 LICENSE 文件。

## 📧 联系信息

- **项目作者**：刘辰
- **GitHub**：https://github.com/santa3-1-1
- **项目地址**：https://github.com/santa3-1-1/Django_blog

## 🙏 致谢

感谢以下开源项目：
- https://www.djangoproject.com/ - Web框架
- https://getbootstrap.com/ - 前端框架
- https://www.python.org/ - 编程语言

---

## 🎯 未来计划

- [ ] 添加文章评论功能
- [ ] 实现文章分类和标签
- [ ] 集成Markdown编辑器
- [ ] 增加全文搜索功能
- [ ] 添加REST API接口
- [ ] 实现第三方登录
- [ ] 添加图片上传功能
- [ ] 实现文章点赞和收藏

## 📈 项目状态

!https://img.shields.io/badge/django-4.2.8-green
!https://img.shields.io/badge/python-3.9+-blue
!https://img.shields.io/badge/license-MIT-yellow
!https://img.shields.io/github/last-commit/santa3-1-1/Django_blog

---
**⭐ 如果这个项目对你有帮助，请点个Star支持！**
