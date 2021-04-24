from django.db import models

# Create your models here.

"""
    1 创建的模型类需要继承自models.Model
    2 系统会为我们自动创建id字段
    3 字段：
        字段名=models.类型(选项)
"""


class BookInfo(models.Model):
    # id
    # varchar(10)
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


# 准备人物列表信息的模型类
class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    # 外键约束：人物属于哪本书
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)
