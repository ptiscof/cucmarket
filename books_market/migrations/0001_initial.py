# Generated by Django 2.2.13 on 2023-05-21 13:13

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=15, unique=True, verbose_name='用户名')),
                ('nickname', models.CharField(blank=True, max_length=13, null=True, verbose_name='昵称')),
                ('age', models.IntegerField(blank=True, null=True, verbose_name='年龄')),
                ('gender', models.CharField(blank=True, choices=[('1', '男'), ('2', '女')], max_length=2, null=True, verbose_name='性别')),
                ('phone', models.CharField(blank=True, max_length=11, null=True, verbose_name='手机号码')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='user_picture', verbose_name='用户头像')),
                ('home_address', models.CharField(blank=True, max_length=100, null=True, verbose_name='地址')),
                ('card_id', models.CharField(blank=True, max_length=30, null=True, verbose_name='身份证')),
                ('is_active', models.BooleanField(default=True, verbose_name='激活状态')),
                ('is_staff', models.BooleanField(default=True, verbose_name='是否是员工')),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('bid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='书名名')),
                ('sold_num', models.IntegerField(default=0, verbose_name='书籍销售量')),
                ('goods_num', models.IntegerField(default=0, verbose_name='库存数')),
                ('market_price', models.FloatField(default=0, verbose_name='市场价格')),
                ('goods_brief', models.TextField(blank=True, max_length=500, null=True, verbose_name='书籍简短描述')),
                ('goods_front_image', models.ImageField(blank=True, null=True, upload_to='books_images', verbose_name='封面图')),
                ('is_new', models.BooleanField(default=False, verbose_name='是否新品')),
                ('is_hot', models.BooleanField(default=False, verbose_name='是否热销')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '商品信息',
                'verbose_name_plural': '商品信息',
            },
        ),
        migrations.CreateModel(
            name='BooksCategory',
            fields=[
                ('bcid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', help_text='类别名', max_length=30, verbose_name='类别名')),
                ('desc', models.TextField(blank=True, help_text='类别描述', null=True, verbose_name='类别描述')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '商品类别',
                'verbose_name_plural': '商品类别',
            },
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('oid', models.AutoField(primary_key=True, serialize=False)),
                ('order_mount', models.FloatField(default=0.0, verbose_name='订单金额')),
                ('address', models.CharField(default='', max_length=100, verbose_name='收货地址')),
                ('signer_name', models.CharField(default='', max_length=20, verbose_name='签收人')),
                ('singer_mobile', models.CharField(max_length=11, verbose_name='联系电话')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '订单信息',
                'verbose_name_plural': '订单信息',
            },
        ),
        migrations.CreateModel(
            name='OrderBooks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_num', models.IntegerField(default=0, verbose_name='商品数量')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books_market.Book', verbose_name='商品')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books_market.OrderInfo', verbose_name='订单信息')),
            ],
            options={
                'verbose_name': '订单商品',
                'verbose_name_plural': '订单商品',
            },
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books_market.BooksCategory', verbose_name='商品类目'),
        ),
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nums', models.IntegerField(default=0, verbose_name='购买数量')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('books', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books_market.Book', verbose_name='商品')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '购物车',
                'verbose_name_plural': '购物车',
                'unique_together': {('user', 'books')},
            },
        ),
    ]
