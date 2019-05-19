from django.shortcuts import render

# Create your views here.

from django.shortcuts import render,get_object_or_404,redirect
from blog.models import Post
from .models import Comment
from .forms import CommentForm

def post_comment(request,post_pk):
    # 先获取被评论的文章，因为后面需要把评论和被评论的文章关联起来。
    # 这里我们使用了 Django 提供的一个快捷函数 get_object_or_404，
    # 这个函数的作用是当获取的文章（Post）存在时，则获取；否则返回 404 页面给用户。
    post=get_object_or_404(Post,pk=post_pk)

    if request.method=='POST':
        form=CommentForm(request.POST)

        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=post
            comment.save()
            return redirect(post)
        else:
            comment_list=post.comment_set.all()
            context={'post':post,'form':form,'comment_list':comment_list}
            return render(request,'blog/detail.html',context=context)

    #首先我们使用了redirect函数。这个函数位于django.shortcuts模块中，它的作用是对
    #HTTP请求进行重定向（即用户访问的是某个URL，但由于某些原因，服务器会将用户重定向到另外的
    #URL）。redirect既可以接收一个URL作为参数，也可以接收一个模型的实例作为参数（例如这里的
    #post）。如果接收一个模型的实例，那么这个实例必须实现了get_absolute_url方法，这样
    #redirect会根据get_absolute_url方法返回的URL值进行重定向。
    return redirect(post)