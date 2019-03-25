from __future__ import unicode_literals
from django.db import models
from DjangoUeditor.models import UEditorField
# Create your models here.

class Article(models.Model):
    title = models.CharField('博客标题',max_length = 100)  #博客标题
    category = models.CharField('博客标签',max_length = 50,blank = True)  #博客标签
    pub_date = models.DateTimeField('发布日期',auto_now_add = True,editable = True)  # 博客发布日期
    update_time = models.DateTimeField('更新日期',auto_now = True,null = True)  #更新时间
    content = UEditorField("文章正文",height=300,width=1000,default=u'',blank=True,imagePath="uploads/blog/images/",
                           toolbars='besttome',filePath='uploads/blog/files/')  #博客正文

    def __unicode__(self):
        return self.title

    class Meta: # 按照时间降序排列
        ordering = ['-pub_date']
        verbose_name = "文章"
        verbose_name_plural = "文章"
