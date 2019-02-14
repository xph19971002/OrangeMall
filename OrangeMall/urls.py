from django.conf import settings
from django.conf.urls import url, include
import xadmin
from django.conf.urls.static import static

from apps.main import views

urlpatterns = [
                  url(r'^xadmin/', xadmin.site.urls),
                  url('^$', views.index, name='index'),
                  url('account/', include('account.urls', namespace='account')),
                  url('detail/', include('detail.urls')),
                  url('main/', include('main.urls')),
                  url(r'^search/', views.MySearchView(),name='search'),
                  url('list/', include('apps.list.urls', namespace='list')),
                  url('car/', include('car.urls')),
                  url('order/', include('order.urls'))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
