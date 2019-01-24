$(function () {
    //点击’+‘实现商品数量递增效果
    $('.add').click(function () {
        //获取商品数量最大值
        let max_num = $(this).next().attr('max');
        //获取商品数量
        let num = $(this).next().val();
        if (parseInt(num) < parseInt(max_num)){
            num ++ ;
            $(this).next().val(num);
        }else {
            $(this).next().val(num);
        }
        // 商品单价
        let single_price = $(this).parent().parent().prev().text();
        // 商品总价
        let total_price = toDecimal2(num * single_price);
        $(this).parent().parent().next().text(total_price);
        let shop_id = $(this).prev().prop('add_shop_id')
    });
    //点击’-‘实现商品数量递减效果
    $('.minus').click(function () {
        //获取商品数量
        let num = $(this).prev().val();
        if (num > 1){
            num -- ;
            $(this).prev().val(num);
        }else {
            $(this).prev().val(num);
        }
        // 商品单价
        let single_price = $(this).parent().parent().prev().text();
        // 商品总价
        let total_price = toDecimal2(num * single_price);
        $(this).parent().parent().next().text(total_price);
    });

    // {#其他类型转化带两位小数的float#}
            function toDecimal2(x) {
            var f = parseFloat(x);
            if (isNaN(f)) {
                return false;
            }
            var f = Math.round(x * 100) / 100;
            var s = f.toString();
            var rs = s.indexOf('.');
            if (rs < 0) {
                rs = s.length;
                s += '.';
            }
            while (s.length <= rs + 2) {
                s += '0';
            }
            return s;
        }

});

// 全选，全不选
$(function () {
    $('#all_check').click(function () {
        if ($(this).prop('checked')){
            $('input[name="checkbox"]').each(function (index,ele) {
                $(ele).prop('checked',true);
            });
        }else {
            $('input[name="checkbox"]').each(function (index,ele) {
                $(ele).prop('checked',false);
            });
        }

    });


    // {#给每一个checkbox添加点击效果#}
    let $sonCheckBox = $('.son_check');
    $sonCheckBox.each(function () {
        $(this).click(function () {
            if ($(this).is(':checked')) {
        //判断：所有单个商品是否勾选
                var len = $sonCheckBox.length;
                var num = 0;
                $sonCheckBox.each(function () {
                    if ($(this).is(':checked')) {
                        num++;
                    }
                });
                if (num === len) {
                    $('#all_check').prop("checked", true);

                }
            } else {
        //单个商品取消勾选，全局全选取消勾选
                $('#all_check').prop("checked", false);

            }
        })
    })
});

$(function () {
    let shop_price = [];
    $('input[name="checkbox"]').each(function (index,ele) {
        if ($(ele).is(':checked')){
            let sing_all = $(ele).parent().nextAll('.single_all').text();
            shop_price.push(sing_all)
        }else {
            shop_price.push(0)
        }
        // let all_price = 0;
        // for (let price of shop_price) {
        //     all_price = all_price + price
        // }
        // $(ele).parents('.table').next().find('#total_price').text(all_price)

    });
    let $em = $('.col03').children('em');
    var all_price = $em.text();
    for (let price of shop_price) {
             all_price = parseInt(all_price) + price
        }
        $em.text(all_price)



});