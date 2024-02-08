from django.urls import path

from Green_app.customer_views import IndexView, Singleproducts, View_Category, CartView, CartView1, CartView2, \
    View_Cart, Checkout, RejectcartView, payment, Direct_checkout, BookingView, Buy_now, Direct_payment, My_Profile

urlpatterns = [

    path('',IndexView.as_view()),
    path('single_view',Singleproducts.as_view()),
    path('view_categ',View_Category.as_view()),
    path('cart',CartView.as_view()),
    path('cart1',CartView1.as_view()),
    path('cart2',CartView2.as_view()),
    path('cart3',Buy_now.as_view()),
    path('view_cart',View_Cart.as_view()),
    path('checkout',Checkout.as_view()),
    path('Direct_checkout',Direct_checkout.as_view()),
    path('removecart',RejectcartView.as_view()),
    path('chpy', payment.as_view()),
    path('booking',BookingView.as_view()),
    path('d_payment',Direct_payment.as_view()),
    path('My_Profile',My_Profile.as_view())

    # path('byenow',Buynow.as_view())


    ]

def urls():
    return urlpatterns, 'customer','customer'