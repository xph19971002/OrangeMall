# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-02-13 14:54
from __future__ import unicode_literals

import apps.main.models
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone', models.CharField(default='110', max_length=11, verbose_name='手机号')),
                ('desc', models.CharField(blank=True, max_length=255, null=True)),
                ('icon', models.ImageField(default='user_icon_img/default.png', upload_to='upload/img/%Y%m%d', verbose_name='头像')),
                ('_paypasswd', models.CharField(max_length=128, verbose_name='支付密码')),
                ('id_num', models.CharField(max_length=128, verbose_name='身份证号')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '用户管理',
                'verbose_name_plural': '用户管理',
                'db_table': 'user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('aid', models.AutoField(primary_key=True, serialize=False, verbose_name='地址ID')),
                ('province', models.CharField(max_length=64, verbose_name='省')),
                ('city', models.CharField(max_length=64, verbose_name='市')),
                ('detail_loc', models.CharField(max_length=255, verbose_name='详细地址')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('is_detele', models.BooleanField()),
                ('user', models.ForeignKey(db_column='uid', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='用户ID')),
            ],
            options={
                'verbose_name': '用户地址',
                'verbose_name_plural': '用户地址',
                'db_table': 'address',
            },
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('banner_id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('image', models.ImageField(storage=apps.main.models.ImageStorage(), upload_to='banner/%Y%m%d', verbose_name='轮播图')),
                ('detail_url', models.CharField(max_length=200, verbose_name='访问地址')),
                ('order', models.IntegerField(default=1, verbose_name='顺序')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('is_delete', models.BooleanField(verbose_name='状态')),
            ],
            options={
                'verbose_name': '轮播图',
                'verbose_name_plural': '轮播图',
                'db_table': 'banner',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('cate_id', models.AutoField(primary_key=True, serialize=False, verbose_name='分类ID')),
                ('parent_id', models.IntegerField(verbose_name='父ID')),
                ('level', models.IntegerField(verbose_name='分类级别')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='商品名称')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='状态')),
            ],
            options={
                'verbose_name': '分类菜单',
                'verbose_name_plural': '菜单管理',
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Collect',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('is_delete', models.BooleanField()),
            ],
            options={
                'verbose_name': '商品收藏',
                'verbose_name_plural': '商品收藏',
                'db_table': 'collect',
            },
        ),
        migrations.CreateModel(
            name='Headline',
            fields=[
                ('hid', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.CharField(max_length=255, verbose_name='信息')),
                ('status', models.BooleanField(verbose_name='状态')),
            ],
            options={
                'verbose_name': '商城头条',
                'verbose_name_plural': '商城头条',
                'db_table': 'headline',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('img_id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=32, null=True, verbose_name='图片类型')),
                ('img_url', models.CharField(max_length=255, verbose_name='图片名称')),
                ('is_delete', models.BooleanField(default=False, verbose_name='状态')),
            ],
            options={
                'verbose_name': '商品图片',
                'verbose_name_plural': '商品图片管理',
                'db_table': 'image',
            },
        ),
        migrations.CreateModel(
            name='Navigation',
            fields=[
                ('nav_id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('nav_name', models.CharField(max_length=64, verbose_name='名称')),
                ('is_delete', models.BooleanField()),
            ],
            options={
                'verbose_name': '导航栏',
                'verbose_name_plural': '导航栏',
                'db_table': 'navigation',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('oid', models.AutoField(primary_key=True, serialize=False, verbose_name='订单ID')),
                ('order_code', models.CharField(max_length=255, verbose_name='订单号')),
                ('address', models.CharField(max_length=255, verbose_name='配送地址')),
                ('postcode', models.CharField(max_length=100, verbose_name='邮编')),
                ('receiver', models.CharField(max_length=100, verbose_name='收货人')),
                ('mobile', models.CharField(max_length=11, verbose_name='手机号')),
                ('user_message', models.CharField(max_length=255, verbose_name='附加信息')),
                ('create_date', models.DateTimeField(max_length=0, verbose_name='创建日期')),
                ('pay_date', models.DateTimeField(blank=True, max_length=0, null=True, verbose_name='支付时间')),
                ('delivery_date', models.DateTimeField(blank=True, verbose_name='交易日期')),
                ('confirm_date', models.DateTimeField(blank=True, verbose_name='确认日期')),
                ('status', models.IntegerField(choices=[(1, '正常'), (0, '异常'), (-1, '删除')], default=1, verbose_name='订单状态')),
                ('user', models.ForeignKey(db_column='uid', on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_order', to=settings.AUTH_USER_MODEL, verbose_name='用户ID')),
            ],
            options={
                'verbose_name': '订单',
                'verbose_name_plural': '订单管理',
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('property_id', models.AutoField(primary_key=True, serialize=False, verbose_name='商品参数名')),
                ('name', models.CharField(max_length=64, verbose_name='属性名称')),
                ('is_delete', models.BooleanField(default=0)),
            ],
            options={
                'verbose_name': '商品属性',
                'verbose_name_plural': '商品属性',
                'db_table': 'property',
            },
        ),
        migrations.CreateModel(
            name='PropertyValue',
            fields=[
                ('pro_value_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=255, verbose_name='属性值')),
                ('is_delete', models.BooleanField(default=False)),
                ('property', models.ForeignKey(db_column='property_id', on_delete=django.db.models.deletion.CASCADE, to='main.Property', verbose_name='属性ID')),
            ],
            options={
                'verbose_name': '商品属性值',
                'verbose_name_plural': '商品属性值',
                'db_table': 'property_value',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('review_id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=4000, verbose_name='内容')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('is_delete', models.BooleanField()),
            ],
            options={
                'verbose_name': '用户评论',
                'verbose_name_plural': '用户评论',
                'db_table': 'review',
            },
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('s_id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=64, verbose_name='品牌')),
                ('type', models.CharField(max_length=64, verbose_name='种类')),
                ('buy_hot', models.CharField(max_length=64, verbose_name='选购热点')),
                ('is_delete', models.BooleanField()),
            ],
            options={
                'db_table': 'search',
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('shop_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='商品ID')),
                ('name', models.CharField(max_length=100, verbose_name='商品名称')),
                ('original_price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='原价')),
                ('promote_price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='折扣价')),
                ('stock', models.IntegerField(verbose_name='库存')),
                ('create_date', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('is_hot', models.BooleanField(default=False, verbose_name='热卖商品')),
                ('sale', models.IntegerField(verbose_name='商品销量')),
                ('sort', models.IntegerField(verbose_name='排序')),
                ('is_delete', models.BooleanField(default=False, verbose_name='商品状态')),
                ('cate', models.ForeignKey(db_column='cate_id', on_delete=django.db.models.deletion.DO_NOTHING, to='main.Category', verbose_name='商品分类')),
            ],
            options={
                'verbose_name': '商品信息',
                'verbose_name_plural': '商品管理',
                'db_table': 'shop',
            },
        ),
        migrations.CreateModel(
            name='ShopCar',
            fields=[
                ('car_id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=0, verbose_name='商品数量')),
                ('status', models.IntegerField(default=1)),
                ('order', models.ForeignKey(db_column='oid', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_shopcar', to='main.Order', verbose_name='商品ID')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='shop_shopcar', to='main.Shop', verbose_name='商品ID')),
                ('user', models.ForeignKey(db_column='uid', on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_shopcar', to=settings.AUTH_USER_MODEL, verbose_name='用户ID')),
            ],
            options={
                'verbose_name': '购物车',
                'verbose_name_plural': '购物车',
                'db_table': 'shop_car',
            },
        ),
        migrations.AddField(
            model_name='search',
            name='shop',
            field=models.ForeignKey(db_column='cate_id', on_delete=django.db.models.deletion.DO_NOTHING, to='main.Shop', verbose_name='商品id'),
        ),
        migrations.AddField(
            model_name='review',
            name='shop',
            field=models.ForeignKey(db_column='shop_id', on_delete=django.db.models.deletion.DO_NOTHING, related_name='shop_review', to='main.Shop', verbose_name='商品ID'),
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(db_column='uid', on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_review', to=settings.AUTH_USER_MODEL, verbose_name='用户ID'),
        ),
        migrations.AddField(
            model_name='property',
            name='shop',
            field=models.ForeignKey(db_column='shop_id', on_delete=django.db.models.deletion.DO_NOTHING, to='main.Shop', verbose_name='商品ID'),
        ),
        migrations.AddField(
            model_name='image',
            name='shop',
            field=models.ForeignKey(db_column='shop_id', on_delete=django.db.models.deletion.DO_NOTHING, to='main.Shop', verbose_name='商品名称'),
        ),
        migrations.AddField(
            model_name='collect',
            name='shop',
            field=models.ForeignKey(db_column='shop_id', on_delete=django.db.models.deletion.CASCADE, related_name='shop_collect', to='main.Shop', verbose_name='商品ID'),
        ),
        migrations.AddField(
            model_name='collect',
            name='user',
            field=models.ForeignKey(db_column='uid', on_delete=django.db.models.deletion.CASCADE, related_name='user_collect', to=settings.AUTH_USER_MODEL, verbose_name='用户ID'),
        ),
    ]
