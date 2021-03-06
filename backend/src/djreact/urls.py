from django.contrib import admin
from django.urls import path, include, re_path
from articles.views import index

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('articles.api.urls')),
    re_path(r'^(?:.*)/?$', index)
]
