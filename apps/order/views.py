from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from apps.main.models import ShopCar


@login_required
def confirm1(request):
    oid = request.GET.get('oid')
    shops = ShopCar.objects.filter(order_id=oid)
    return render(request, 'confirm.html', {'shops': shops})
