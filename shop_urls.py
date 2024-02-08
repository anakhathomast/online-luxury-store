from django.urls import path

from Green_app.shop_views import IndexView, Addproduct, View_Product, Delete_product,BookingView

urlpatterns = [

    path('',IndexView.as_view()),
    path('addproduct', Addproduct.as_view()),
    path('product_view', View_Product.as_view()),
    path('delete', Delete_product.as_view()),
    path('booking', BookingView.as_view())

]

def urls():
    return urlpatterns, 'shop','shop'


