from django.shortcuts import render, redirect

# Create your views here.
from alipay import AliPay

from OrangeMall.settings import APP_ID, APP_PRIVATE_KEY_STR, APP_PUBLIC_KEY_STR, PAY_URL_DEV

def alipay(request):
    alipay = AliPay(
        # 实例化Alipay对象
        appid=APP_ID,
        app_notify_url=None,
        app_private_key_string=APP_PRIVATE_KEY_STR,
        alipay_public_key_string=APP_PUBLIC_KEY_STR,
        sign_type='RSA',
        debug=True,
    )

    # 生成支付的参数
    '''
    subject 支付的标题
    out_trade_no 生成的订单号
    total_amount 支付的总金额
    return_url  支付完成之后前端跳转的界面 get请求
    notify_url 支付完成后台回调接口  post请求
    '''
    order_str = alipay.api_alipay_trade_page_pay(
        subject=10,
        out_trade_no=2,
        total_amount=123,
        return_url='https:www.baidu.com',
    )
    return redirect(PAY_URL_DEV + '?' + order_str)