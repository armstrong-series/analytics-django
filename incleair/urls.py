
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import serve
from django.urls import path, include, re_path

urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    # path('admin/', admin.site.urls),
    path('', include('analytics.urls')),
    path('api/chart/', include('analytics.urls')),
    path('incleair/dashboard/', include('analytics.urls'))

]

