from django.db import models

# Create your models here.


class UserInfo(models.Model):
    username = models.CharField(verbose_name='用户名', max_length=32, db_index=True)
    email = models.EmailField(verbose_name='邮箱', max_length=32)
    mobile_phone = models.CharField(verbose_name='手机号', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=32)


class Student_Information(models.Model):
    # 姓名
    name = models.CharField(max_length=200)

    # 学号
    address = models.CharField(max_length=200)

    # 图片
    img = models.ImageField(upload_to='img')


class Distinguish(models.Model):
    # 学生状态
    state = models.CharField(max_length=200)

    # 识别人数
    Number = models.BigIntegerField()

    # 具体信息
    specific = models.TextField(blank=True, null=True)


class Eachclass(models.Model):
    # 第几节课
    Thatclass = models.CharField(max_length=200)
    # 认真听讲人数
    Earnestpeopl = models.BigIntegerField()
    # 平均专注度值
    Focusvalue = models.BigIntegerField()
