from django.shortcuts import render

# Create your views here.
from apps.main.models import ShopCar


def car_list(request):
    # 获取用户购物车列表
    cars = ShopCar.objects.filter(shop_id=request.user.id)
    for car in cars:
        # 商品图片
        car.image = car.shop.image_set.filter(shop_id=car.shop.shop_id).first()
        # 商品总价
        car.sum_price = car.shop.promote_price * car.number
    return render(request,'car.html',context={'cars':cars})


