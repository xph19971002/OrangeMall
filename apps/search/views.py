import random

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from apps.main.models import Shop, Image, Property, Category


def search(request):
    cate_1 = Category.objects.filter(level=2).values('name')
    cate_1 = random.sample(list(cate_1),8)
    cate_2 = Category.objects.filter(level=3).values('name')
    cate_2 = random.sample(list(cate_2), 8)
    cate_3 = Shop.objects.all().values('name')
    cate_3 = random.sample(list(cate_3),5)
    shops = Shop.objects.all().values('name', 'original_price','sale','shop_id')
    shop_numbers = Shop.objects.all().count()
    for shop in shops:
        img = Image.objects.filter(shop_id=shop.get('shop_id')).values('img_url').first()
        shop['img_url'] = img['img_url']

    p = Paginator(shops, 12)  # 分页，10篇文章一页
    if p.num_pages <= 1:  # 如果文章不足一页
        shop_list = shops  # 直接返回所有文章
        data= {}  # 不需要分页按钮
    else:
        page = int(request.GET.get('page', 1))  # 获取请求的文章页码，默认为第一页
        shop_list = p.page(page)  # 返回指定页码的页面
        left = []  # 当前页左边连续的页码号，初始值为空
        right = []  # 当前页右边连续的页码号，初始值为空
        left_has_more = False  # 标示第 1 页页码后是否需要显示省略号
        right_has_more = False  # 标示最后一页页码前是否需要显示省略号
        first = False  # 标示是否需要显示第 1 页的页码号。
        # 因为如果当前页左边的连续页码号中已经含有第 1 页的页码号，此时就无需再显示第 1 页的页码号，
        # 其它情况下第一页的页码是始终需要显示的。
        # 初始值为 False
        last = False  # 标示是否需要显示最后一页的页码号。
        total_pages = p.num_pages
        page_range = p.page_range
        if page == 1:  # 如果请求第1页
            right = page_range[page:page + 2]  # 获取右边连续号码页
            if right[-1] < total_pages - 1:  # 如果最右边的页码号比最后一页的页码号减去 1 还要小，
                # 说明最右边的页码号和最后一页的页码号之间还有其它页码，因此需要显示省略号，通过 right_has_more 来指示。
                right_has_more = True
            if right[-1] < total_pages:  # 如果最右边的页码号比最后一页的页码号小，说明当前页右边的连续页码号中不包含最后一页的页码
                # 所以需要显示最后一页的页码号，通过 last 来指示
                last = True
        elif page == total_pages:  # 如果请求最后一页
            left = page_range[(page - 3) if (page - 3) > 0 else 0:page - 1]  # 获取左边连续号码页
            if left[0] > 2:
                left_has_more = True  # 如果最左边的号码比2还要大，说明其与第一页之间还有其他页码，因此需要显示省略号，通过 left_has_more 来指示
            if left[0] > 1:  # 如果最左边的页码比1要大，则要显示第一页，否则第一页已经被包含在其中
                first = True
        else:  # 如果请求的页码既不是第一页也不是最后一页
            left = page_range[(page - 3) if (page - 3) > 0 else 0:page - 1]  # 获取左边连续号码页
            right = page_range[page:page + 2]  # 获取右边连续号码页
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
        data = {  # 将数据包含在data字典中

            'left': left,
            'right': right,
            'left_has_more': left_has_more,
            'right_has_more': right_has_more,
            'first': first,
            'last': last,
            'total_pages': total_pages,
            'page': page
        }
    return render(request,'search_page.html',locals())

def search_result(request):
    cate_1 = Category.objects.filter(level=2).values('name')
    cate_1 = random.sample(list(cate_1), 8)
    cate_2 = Category.objects.filter(level=3).values('name')
    cate_2 = random.sample(list(cate_2), 8)
    cate_3 = Shop.objects.all().values('name')
    cate_3 = random.sample(list(cate_3), 5)
    if request.method == 'GET':
        q = request.GET.get('search')
        if q:
            shops = Shop.objects.filter(name__contains=q).values('name', 'original_price', 'sale', 'shop_id')
            shop_numbers = Shop.objects.filter(name__contains=q).count()
            for shop in shops:
                img = Image.objects.filter(shop_id=shop.get('shop_id')).values('img_url').first()
                shop['img_url'] = img['img_url']

            p = Paginator(shops, 12)  # 分页，10篇文章一页
            if p.num_pages <= 1:  # 如果文章不足一页
                shop_list = shops  # 直接返回所有文章
                data = {}
            else:
                page = int(request.GET.get('page', 1))  # 获取请求的文章页码，默认为第一页
                shop_list = p.page(page)  # 返回指定页码的页面
                left = []  # 当前页左边连续的页码号，初始值为空
                right = []  # 当前页右边连续的页码号，初始值为空
                left_has_more = False  # 标示第 1 页页码后是否需要显示省略号
                right_has_more = False  # 标示最后一页页码前是否需要显示省略号
                first = False  # 标示是否需要显示第 1 页的页码号。
                # 因为如果当前页左边的连续页码号中已经含有第 1 页的页码号，此时就无需再显示第 1 页的页码号，
                # 其它情况下第一页的页码是始终需要显示的。
                # 初始值为 False
                last = False  # 标示是否需要显示最后一页的页码号。
                total_pages = p.num_pages
                page_range = p.page_range
                if page == 1:  # 如果请求第1页
                    right = page_range[page:page + 2]  # 获取右边连续号码页
                    if right[-1] < total_pages - 1:  # 如果最右边的页码号比最后一页的页码号减去 1 还要小，
                        # 说明最右边的页码号和最后一页的页码号之间还有其它页码，因此需要显示省略号，通过 right_has_more 来指示。
                        right_has_more = True
                    if right[-1] < total_pages:  # 如果最右边的页码号比最后一页的页码号小，说明当前页右边的连续页码号中不包含最后一页的页码
                        # 所以需要显示最后一页的页码号，通过 last 来指示
                        last = True
                elif page == total_pages:  # 如果请求最后一页
                    left = page_range[(page - 3) if (page - 3) > 0 else 0:page - 1]  # 获取左边连续号码页
                    if left[0] > 2:
                        left_has_more = True  # 如果最左边的号码比2还要大，说明其与第一页之间还有其他页码，因此需要显示省略号，通过 left_has_more 来指示
                    if left[0] > 1:  # 如果最左边的页码比1要大，则要显示第一页，否则第一页已经被包含在其中
                        first = True
                else:  # 如果请求的页码既不是第一页也不是最后一页
                    left = page_range[(page - 3) if (page - 3) > 0 else 0:page - 1]  # 获取左边连续号码页
                    right = page_range[page:page + 2]  # 获取右边连续号码页
                    if left[0] > 2:
                        left_has_more = True
                    if left[0] > 1:
                        first = True
                    if right[-1] < total_pages - 1:
                        right_has_more = True
                    if right[-1] < total_pages:
                        last = True
                data = {  # 将数据包含在data字典中
                    'left': left,
                    'right': right,
                    'left_has_more': left_has_more,
                    'right_has_more': right_has_more,
                    'first': first,
                    'last': last,
                    'total_pages': total_pages,
                    'page': page
                }
            return render(request, 'search_result.html', locals())
        else:
            return render(request, 'search_page.html', locals())
    else:
        return render(request,'search_page.html',locals())
