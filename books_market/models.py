from datetime import datetime

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

class UserManager(BaseUserManager): #自定义Manager管理器
    def _create_user(self,username,password,**kwargs):
        if not username:
            raise ValueError("请传入用户名！")
        if not password:
            raise ValueError("请传入密码！")
        user = self.model(username=username,**kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_user(self,username,password,**kwargs): # 创建普通用户
        kwargs['is_superuser'] = False
        return self._create_user(username,password,**kwargs)

    def create_superuser(self,username,password,**kwargs): # 创建超级用户
        kwargs['is_superuser'] = True
        kwargs['is_staff'] = True
        return self._create_user(username,password,**kwargs)

class User(AbstractUser): # 自定义User
    GENDER_TYPE = (
        ("1","男"),
        ("2","女")
    )
    uid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=15,verbose_name="用户名",unique=True)
    nickname = models.CharField(max_length=13,verbose_name="昵称",null=True,blank=True)
    age = models.IntegerField(verbose_name="年龄",null=True,blank=True)
    gender = models.CharField(max_length=2,choices=GENDER_TYPE,verbose_name="性别",null=True,blank=True)
    phone = models.CharField(max_length=11,null=True,blank=True,verbose_name="手机号码")
    email = models.EmailField(verbose_name="邮箱",null=True,blank=True)
    picture = models.ImageField(upload_to="media/users/images",verbose_name="用户头像",null=True,blank=True)
    home_address = models.CharField(max_length=100,null=True,blank=True,verbose_name="地址")
    card_id = models.CharField(max_length=30,verbose_name="身份证",null=True,blank=True)
    is_active = models.BooleanField(default=True,verbose_name="激活状态")
    is_staff = models.BooleanField(default=False,verbose_name="是否是员工")
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'username' # 使用authenticate验证时使用的验证字段，可以换成其他字段，但验证字段必须是唯一的，即设置了unique=True
    EMAIL_FIELD = 'email' # 发送邮件时使用的字段

    objects = UserManager()

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

class Category(models.Model):
    cid = models.AutoField(primary_key=True)
    name = models.CharField('类别名', default="", max_length=30, help_text="类别名")
    desc = models.TextField("类别描述",help_text="类别描述",null=True,blank=True,)
    add_time = models.DateTimeField("添加时间", default=datetime.now)

    class Meta:
        verbose_name = "书籍类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Book_Category(models.Model):
    '''书籍：类别 = N：N'''
    bid = models.ForeignKey('Book',on_delete=models.CASCADE,verbose_name='书籍')
    cid = models.ForeignKey(Category,on_delete=models.SET(0),verbose_name='类别')

    def __str__(self):
        return f'{self.bid.name}--{self.cid.name}'

class Book(models.Model):
    """书籍"""
    bid = models.AutoField(primary_key=True)
    cid = models.ManyToManyField(Category,through=Book_Category,through_fields=('bid','cid'))
    name = models.CharField("书名", max_length=100, )
    sold_num = models.IntegerField("书籍销售量", default=0)
    books_num = models.IntegerField("库存数", default=0)
    market_price = models.FloatField("市场价格", default=0)
    books_brief = models.TextField("书籍简短描述", max_length=500,null=True,blank=True)
    # 首页中展示的商品封面图
    books_front_image = models.ImageField(upload_to='media/books/images', null=True, blank=True, verbose_name="封面图")
    # 首页中新品展示
    is_new = models.BooleanField("是否新品", default=False)
    # 商品详情页的热卖商品，自行设置
    is_hot = models.BooleanField("是否热销", default=False)
    add_time = models.DateTimeField("添加时间", default=datetime.now)
    class Meta:
        verbose_name = '书籍信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.bid}  {self.name}  {[card.name for card in self.cid.all()]}'


