from django.db import models

# Create your models here.
#分类
class Category(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

#标签
class Tag(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

from django.utils.six import python_2_unicode_compatible
from django.contrib.auth.models import User
from django.urls import reverse
#文章
@python_2_unicode_compatible
class Post(models.Model):
    title=models.CharField(max_length=70)
    body=models.TextField()

    #这两个列分别表示文章的创建时间和最后一次修改时间，存储时间的字段
    #用DataTimeField类型
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    #文章摘要，指定charfied_time的blank=true，参数值后可以允许空值了
    excerpt = models.CharField(max_length=200,blank=True)

    #分类，一对多，外键
    category = models.ForeignKey(Category)
    #标签，多对多
    tags = models.ManyToManyField(Tag)

    #文章作者，这里的user是从django.contrib.auth.models导入的
    #django.contrib.auth是从django内置的应用，专门用于处理网站用户的注册
    #通过外键把文章和user关联起来，一对多
    author = models.ForeignKey(User)
    def __str__(self):
        return self.title
    #设定的name='detail'在这里派上了用场。这个reverse函数，它的
    #第一个参数的值为‘blog：detail’，意思是blog应用下的
    #name=detail的函数，由于我们在上面通过app_name=blog告诉了django这个
    #url模块是属于blog应用的，因此django能够顺利地找到blog应用下name为
    #detail的试图函数
    def get_absolute_url(self):
        return reverse('blog:detail',kwargs={'pk':self.pk})

    class Meta:
        ordering = ['-created_time','title']

