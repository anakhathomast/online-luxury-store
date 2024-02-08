from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.views.generic import TemplateView

from Green_app.models import Product, Categ, Seller_Reg, Cart


class IndexView(TemplateView):
    template_name = 'shop/shop_index.html'


class Addproduct(TemplateView):
    template_name ='shop/add_product.html'

    def get_context_data(self, **kwargs):
        context = super(Addproduct, self).get_context_data(**kwargs)
        category = Categ.objects.all()
        context['category'] = category
        return context

    def post(self, request,*args,**kwargs):
        re = Seller_Reg.objects.get(user_id=self.request.user.id)
        name = request.POST['name']

        category = request.POST['category']
        price = request.POST['price']
        desc = request.POST['desc']
        stock = request.POST['stock']
        image = request.FILES['image']
        fii = FileSystemStorage()
        filesss = fii.save(image.name, image)

        se = Product()
        se.seller_id=re.id
        se.name = name
        se.image=filesss
        se.catg_id = category
        se.stock = stock
        se.price = price
        se.desc = desc

        se.save()

        return render(request, 'shop/shop_index.html', {'message': "Successfully added"})


class View_Product(TemplateView):
    template_name = 'shop/product_view.html'
    def get_context_data(self, **kwargs):
        context = super(View_Product, self).get_context_data(**kwargs)
        re = Seller_Reg.objects.get(user_id=self.request.user.id)

        view_pp = Product.objects.filter(seller_id=re.id)
        context['view_pp'] = view_pp
        return context

class Delete_product(TemplateView):
    def dispatch(self,request,*args,**kwargs):
        id = request.GET['id']
        Product.objects.get(id=id).delete()

        return render(request, 'shop/shop_index.html', {'message': "Deleted"})

class BookingView(TemplateView):
    template_name = 'shop/booking_view.html'
    def get_context_data(self, **kwargs):
        context = super(BookingView,self).get_context_data(**kwargs)
        re = Seller_Reg.objects.get(user_id=self.request.user.id)

        view_b = Cart.objects.filter(status='paid',delivery='paid',seller_id=re.id)

        context['view_b'] = view_b
        return context