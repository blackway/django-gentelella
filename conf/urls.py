"""gentella URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin

import sakila
from . import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # app/ -> Genetelella UI and resources
    url(r'^app/', include('app.urls')),
    url(r'^sakila/', include('sakila.urls')),
    url(r'^', include('sakila.urls')),
    # url(r'^', include('app.urls')),
    url(r'^api-auth/', include('rest_framework.urls')),
    path('api/film/', sakila.views.FilmListApi.as_view()),
    path('api/film/<int:pk>', sakila.views.FilmDetailApi.as_view()),
    # url(r'^api/film/$', sakila.views.FilmListApi.as_view()),
    # url(r'^api/film(?P<pk>[-\w]+)/$', sakila.views.FilmDetailApi.as_view()),
]

if settings.DEBUG:
    # 장고 디버그 툴바 Django Debug Toolbar 쿼리 디버그
    import debug_toolbar
    urlpatterns = [
        url('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns