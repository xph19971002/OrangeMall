from django.shortcuts import render

from apps.main.models import Image,Shop,Property,Category


# Create your views here.


def detail(request):
    if request.method == 'GET':
        # 1174487
        shop_id = request.GET.get("id")
        shop_id = int(shop_id)
        # #商品图片列表
        r = Image.objects.filter(shop_id=shop_id).values("img_url")
        imgs = [img for img in r][:4]
        imgs_first = imgs[0].get("img_url")
        # 商品对象
        shop = Shop.objects.filter(shop_id=shop_id)
        # 商品属性
        property = Property.objects.filter(shop_id=shop_id).all()
        #分类
        cate3 = Category.objects.filter(cate_id=shop.values("cate_id"))
        cate_name3 = cate3.first().name

        return render(request, 'detail.html', locals())

