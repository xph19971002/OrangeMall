# 全局配置
import xadmin
from xadmin import views

from apps.main.models import Navigation, User


class BaseStyleSettings:
    # 开启修改主题
    enable_themes = True
    # 使用bootbootstarp的主题
    use_bootswatch = True


# 注册自定义全局配置
xadmin.site.register(views.BaseAdminView, BaseStyleSettings)


class GlobalSettings:
    site_title = r'橘子商城'
    site_footer = r'橘子，爱你所爱'


xadmin.site.register(views.CommAdminView, GlobalSettings)


class NavigationXadmin:
    # pass
    # 默认情况下显示object对象
    list_display = ['nav_id', 'nav_name']


xadmin.site.register(Navigation, NavigationXadmin)

#
# class UserXadmin:
#     list_display = ['id', 'username']
#
#
# xadmin.site.register(User, UserXadmin)
