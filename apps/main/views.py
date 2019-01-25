from django.http import HttpResponse
from django.shortcuts import render

from apps.main.models import Category, Headline, Banner, ShopCar, Shop


def index(request):
    head_list = Headline.objects.all()
    banner_list = Banner.objects.all()
    hot_list = Shop.objects.filter(is_hot=0)[:4]
    for hot_shop in hot_list:
        hot_shop.image = hot_shop.image_set.filter(type='big').first()
    cate_list = Category.objects.filter(level=1)
    shop_car_queryset = ShopCar.objects.filter(shop_id=request.user.id)
    shop_car_num = shop_car_queryset.count() if shop_car_queryset.exists() else 0
    for cate in cate_list:
        sub_menus = Category.objects.filter(parent_id=cate.cate_id, level=2)
        for sub_menu in sub_menus:
            sub_menus2 = Category.objects.filter(parent_id=sub_menu.cate_id, level=3)
            sub_menu.sub_menus2 = sub_menus2
        cate.sub_menus = sub_menus

    sub_cates = Category.objects.filter(level=3)[:30]
    sub_list = []
    for sub_cate in sub_cates:
        shops = sub_cate.shop_set.all()
        if len(shops):
            sub_list.append(sub_cate)
            for shop in shops:
                shop.image = shop.image_set.all().first()
            sub_cate.shops = shops
    return render(request, 'index.html', locals())
