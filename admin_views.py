from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.views.generic.base import View

from Green_app.models import Product, Categ, Customer_Reg, Feedback, Cart,Seller_Reg


class IndexView(TemplateView):
    template_name = 'admin/admin_index.html'

class Customer_approvel(TemplateView):
    template_name = 'admin/customer_view.html'

    def get_context_data(self, **kwargs):
        context = super(Customer_approvel,self).get_context_data(**kwargs)

        custr = Customer_Reg.objects.filter(user__last_name='0',user__is_staff='0',user__is_active='1')

        context['custr'] = custr
        return context
class Seller_approvel(TemplateView):
    template_name = 'admin/seller_view.html'

    def get_context_data(self, **kwargs):
        context = super(Seller_approvel,self).get_context_data(**kwargs)

        custr = Seller_Reg.objects.filter(user__last_name='0',user__is_staff='0',user__is_active='1')

        context['custr'] = custr
        return context



class ApproveView(View):
    def dispatch(self, request, *args, **kwargs):

        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name='1'
        user.save()
        return render(request,'admin/admin_index.html',{'message':" Account Approved"})


class Add_category(TemplateView):
    template_name='admin/add_category.html'

    def post(self, request, *args, **kwargs):
        name=request.POST['name']
        categ=Categ()
        categ.name=name
        categ.save()
        return redirect(request.META['HTTP_REFERER'],{'message':"Category Successfuly Added"})




class View_Product(TemplateView):
    template_name = 'admin/product_view.html'
    def get_context_data(self, **kwargs):
        context = super(View_Product, self).get_context_data(**kwargs)
        view_pp = Product.objects.all()
        context['view_pp'] = view_pp
        return context



class Feedback_view(TemplateView):
    template_name = 'admin/view_feedback.html'

    def get_context_data(self, **kwargs):
        context = super(Feedback_view, self).get_context_data(**kwargs)

        feed = Feedback.objects.all
        context['feed'] = feed

        return context


class BookingView(TemplateView):
    template_name = 'admin/booking_view.html'
    def get_context_data(self, **kwargs):
        context = super(BookingView,self).get_context_data(**kwargs)
        view_b = Cart.objects.filter(status='paid',delivery='delivered')

        context['view_b'] = view_b
        return context