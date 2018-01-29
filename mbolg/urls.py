from django.conf.urls import include, url
from django.contrib import admin

from mainsite.views import homepage,showpost

urlpatterns = [
    url(r'^$', homepage),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^post/(\w+)$', showpost),
]
