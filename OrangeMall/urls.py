from django.conf.urls import url, include
import xadmin

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url('account/', include('account.urls')),
    url('detail/', include('detail.urls')),
    url('main/', include('main.urls')),
    url('search/', include('search.urls')),
]
