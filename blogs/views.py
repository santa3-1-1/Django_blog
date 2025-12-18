from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.contrib.auth import views as auth_views
from .forms import BlogPostForm, UserProfileForm


from django.core.paginator import Paginator
from django.shortcuts import render
from .models import BlogPost  # 确保导入的是 BlogPost 模型

def home(request):
    posts_list = BlogPost.objects.all().order_by('-date_added')  # 获取所有帖子并按时间排序

    # 确保 posts_list 不为空，分页依然能正常工作
    paginator = Paginator(posts_list, 5)  # 每页5篇文章
    page_number = request.GET.get('page')  # 获取当前页数
    page_obj = paginator.get_page(page_number)  # 获取当前页的数据

    return render(request, 'blogs/home.html', {'page_obj': page_obj})

@login_required
def new_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.user = request.user
            blog_post.save()
            return redirect('home')
    else:
        form = BlogPostForm()
    return render(request, 'blogs/new_post.html', {'form': form})

@login_required
def edit_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if post.user != request.user:
        return redirect('home')
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blogs/edit_post.html', {'form': form})

def delete_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if post.user == request.user:
        post.delete()
    return redirect('home')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'blogs/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def profile(request):
    user = request.user
    posts = BlogPost.objects.filter(user=user).order_by('-date_added')
    return render(request, 'blogs/profile.html', {
        'user': user,
        'posts': posts
    })

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'blogs/edit_profile.html', {'form': form})

class CustomLoginView(auth_views.LoginView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('profile')
        return super().get(request, *args, **kwargs)