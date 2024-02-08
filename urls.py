"""Green_Cart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from django.urls import path

from Green_app import admin_urls, customer_urls, shop_urls
from Green_app.views import IndexView, Users_reg,Login1,seller_registartion

urlpatterns = [
    path('admin/', admin_urls.urls()),
    path('customer/', customer_urls.urls()),
    path('shop/',shop_urls.urls()),
    path('',IndexView.as_view()),
    path('users_reg',Users_reg.as_view()),

    path('login/',Login1.as_view()),
    path('seller_reg',seller_registartion.as_view())
]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)