from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'blogs/index.html')

@login_required
def posts(request):
    """Список постов"""    
    posts = Post.objects.filter(owner=request.user).order_by('date_added')
    context = {'posts' : posts}
    return render(request, 'blogs/posts.html', context)

@login_required
def post(request, post_id):
    """Выводит один пост и все его записи."""
    post = Post.objects.get(id=post_id)
    # Проверка того, что тема принадлежит текущему пользователю.
    if post.owner != request.user:
        raise Http404
    comments = post.comment_set.order_by('-date_added')
    context = {'post' : post, 'comments' : comments}
    return render(request, 'blogs/post.html', context)

@login_required
def new_post(request):
    """Определяет новый пост."""
    if request.method != 'POST':
        form = PostForm()
    else:
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return HttpResponseRedirect(reverse('blogs:posts'))
    
    context = {'form' : form}
    return render(request, 'blogs/new_post.html', context)

@login_required
def new_comment(request, post_id):
    """Добавляет новую запись по конкретной теме."""
    post = Post.objects.get(id=post_id)

    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return HttpResponseRedirect(reverse('blogs:post', args=[post_id]))
    
    context = {'post' : post, 'form' : form}
    return render(request, 'blogs/new_comment.html', context)

@login_required
def edit_comment(request, comment_id):
    """Редактирует существующую запись."""
    comment = Comment.objects.get(id=comment_id)
    post = comment.post
    if post.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Исходный запрос; форма заполняется данными текущей записи. 
        form = CommentForm(instance=comment)
    else:
        # Отправка данных POST; обработать данные.
        form = CommentForm(instance=comment, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs:post', args=[post.id]))
        
    context = {'comment' : comment, 'post' : post, 'form' : form}
    return render(request, 'blogs/edit_comment.html', context)
        



