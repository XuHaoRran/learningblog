from comments.forms import CommentForm
from django.shortcuts import render,get_object_or_404
from .models import Post
# Create your views here.
from django.http import HttpResponse
def index(requset):
    post_list=Post.objects.all().order_by('-created_time')
    print(post_list)
    return render(requset,'blog/index.html',context={
        'title':'我的博客首页','welcome':'欢迎访问我的博客首页',
        'post_list':post_list
    })
import markdown
#使用markdown语法来书写博文。markdown的渲染器能够把我们写的文章转换为标准
#html文档，从而让我们的文章呈现更加丰富的格式。
def detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    #记得在顶部引入markdown模块
    post.body = markdown.markdown(post.body,extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',    #语法高亮拓展
        'markdown.extensions.toc'             #自动生成目录
    ])

    form=CommentForm()
    comment_list =post.comment_set.all().order_by('-created_time')
    context={'post':post,
             'form':form,
             'comment_list':comment_list}
    return render(request,'blog/detail.html',context=context)



def archives(request,year,month):
    post_list=Post.objects.filter(created_time__year=year,
                                  created_time__month=month).order_by('-created_time')
    return render(request,'blog/index.html',context={'post_list':post_list})


