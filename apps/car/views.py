from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from apps.main.models import ShopCar


@login_required
def car_list(request):
    id = request.user.id
    # 获取用户购物车列表
    cars = ShopCar.objects.filter(user=request.user.id)
    for car in cars:
        # 商品图片
        car.image = car.shop.image_set.filter(shop_id=car.shop.shop_id).first()
        # 商品总价
        car.sum_price = float(car.shop.promote_price) * car.number
        car.shop_name = car.shop.name[:6]
    return render(request,'car.html',context={'cars':cars})


