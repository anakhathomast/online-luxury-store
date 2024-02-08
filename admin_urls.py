from django.urls import path

from Green_app.admin_views import IndexView, Add_category, View_Product, Customer_approvel, ApproveView, Feedback_view, \
    BookingView, Seller_approvel

urlpatterns = [

    path('',IndexView.as_view()),
    path('category',Add_category.as_view()),
    path('product_view',View_Product.as_view()),
    path('cus_approve',Customer_approvel.as_view()),
    path('approve', ApproveView.as_view()),
    path('Feedback_view',Feedback_view.as_view()),
    path('booking',BookingView.as_view()),
    path('Seller_approvel',Seller_approvel.as_view())

]

def urls():
    return urlpatterns, 'admin','admin'


