
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from Green_app.models import Product, Categ, Cart, Checkout_details, Feedback, Customer_Reg, Seller_Reg


class IndexView(TemplateView):
    template_name = 'users/product_view.html'
    def get_context_data(self, **kwargs):
        context = super(IndexView,self).get_context_data(**kwargs)
        view_pp = Product.objects.all()
        category = Categ.objects.all()
        context['category'] = category
        context['view_pp'] = view_pp
        return context

class CartView(TemplateView):
    template_name = 'users/product_view.html'
    def dispatch(self,request,*args,**kwargs):
        pid = request.GET['id']
        product = Product.objects.get(pk=pid)
        price = product.price
        quantity = 1
        Total = quantity * int(price)
        product.stock = int(product.stock) - int(quantity)
        product.save()

        ca = Cart()
        shop_reg = Seller_Reg.objects.get(id=product.seller_id)

        ca.user = User.objects.get(id=self.request.user.id)
        ca.seller_id=shop_reg.id
        ca.product = Product.objects.get(pk=pid)
        ca.payment = 'null'
        ca.total=Total
        ca.quantity = quantity

        ca.status = 'cart'
        ca.delivery = 'null'
        ca.save()
        return redirect(request.META['HTTP_REFERER'],{'message':"cart"})

class Singleproducts(TemplateView):
    template_name = 'users/single_product.html'

    def get_context_data(self, **kwargs):
        id = self.request.GET['id']

        context = super(Singleproducts, self).get_context_data(**kwargs)

        single_view = Product.objects.get(id=id)

        context['single_view'] = single_view

        return context

    def post(self, request, *args, **kwargs):
        user = User.objects.get(id=self.request.user.id)

        id2=request.POST['product_id']
        print(id2,'hggvjkjkj')
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        feedback = request.POST['feedback']
        fe = Feedback()
        fe.user = user
        fe.product_id=id2

        fe.name = name
        fe.email = email
        fe.subject = subject
        fe.feedback = feedback
        fe.save()
        return redirect(request.META['HTTP_REFERER'])

class CartView1(TemplateView):
    template_name = 'users/single_product.html'

    def dispatch(self, request, *args, **kwargs):
        pid = request.GET['id']
        product = Product.objects.get(pk=pid)
        price = product.price
        quantity = 1
        Total = quantity * int(price)
        product.stock = int(product.stock) - int(quantity)
        product.save()

        ca = Cart()
        shop_reg = Seller_Reg.objects.get(id=product.seller_id)

        ca.user = User.objects.get(id=self.request.user.id)
        ca.seller_id = shop_reg.id
        ca.product = Product.objects.get(pk=pid)
        ca.payment = 'null'
        ca.total = Total
        ca.quantity = quantity

        ca.status = 'cart'
        ca.delivery = 'null'
        ca.save()
        return redirect(request.META['HTTP_REFERER'], {'message': "cart"})

class View_Category(TemplateView):
    template_name = 'users/category_view.html'
    def get_context_data(self, **kwargs):
        cat_id = self.request.GET['catg_id']
        context = super(View_Category,self).get_context_data(**kwargs)
        category = Categ.objects.all()
        view_ct = Product.objects.filter(catg_id=cat_id)
        context['category'] = category
        context['view_pp'] = view_ct
        return context


class CartView2(TemplateView):
    template_name = 'users/category_view.html'

    def dispatch(self, request, *args, **kwargs):
        pid = request.GET['id']
        product = Product.objects.get(pk=pid)
        price = product.price
        quantity = 1
        Total = quantity * int(price)
        product.stock = int(product.stock) - int(quantity)
        product.save()

        ca = Cart()
        shop_reg = Seller_Reg.objects.get(id=product.seller_id)

        ca.user = User.objects.get(id=self.request.user.id)
        ca.seller_id = shop_reg.user_id
        ca.product = Product.objects.get(pk=pid)
        ca.payment = 'null'
        ca.total = Total
        ca.quantity = quantity

        ca.status = 'cart'
        ca.delivery = 'null'
        ca.save()
        return redirect(request.META['HTTP_REFERER'], {'message': "cart"})

class View_Cart(TemplateView):
    template_name = 'users/cart.html'

    def get_context_data(self, **kwargs):
        context = super(View_Cart, self).get_context_data(**kwargs)
        # user = User.objects.get(id=self.request.user.id)
        cr = self.request.user.id
        ct = Cart.objects.filter(status='cart', user_id=cr, delivery='null')

        total = 0
        for i in ct:
            total = total + int(i.product.price)

        context['ct'] = ct
        context['asz'] = total

        return context

class RejectcartView(TemplateView):
    def dispatch(self,request,*args,**kwargs):
        id = request.GET['id']
        Cart.objects.get(id=id).delete()


        return redirect(request.META['HTTP_REFERER'],{'message':"cart"})


class Buy_now(TemplateView):
    template_name = 'users/single_product.html'

    def dispatch(self, request, *args, **kwargs):
        pid = request.GET['id']
        product = Product.objects.get(pk=pid)
        try:

            if Cart.objects.filter(product_id=product.id, user_id=self.request.user.id, status='buy'):
                return render(request, 'users/checkout1.html', {'message': "already added"})

            else:

                ca = Cart()

                price = product.price
                quantity = 1
                Total = quantity * int(price)
                product.stock = int(product.stock) - int(quantity)
                product.save()
                ca.user = User.objects.get(id=self.request.user.id)
                # ca.shop_id=shop.user_id
                ca.product = Product.objects.get(pk=pid)
                ca.payment = 'null'
                ca.status = 'buy'
                ca.total=Total
                ca.quantity=quantity

                ca.delivery = 'null'
                ca.save()
                ctlr = Cart.objects.filter(status='buy')

                return render(request, 'users/checkout1.html', {'message': "", 'ctlr': ctlr})
        except:

            ca = Cart()
            # shop=Product.objects.get(pk = pid)

            ca.user = User.objects.get(id=self.request.user.id)
            # ca.shop_id=shop.user_id
            ca.product = Product.objects.get(pk=pid)
            ca.payment = 'null'
            ca.status = 'buy'
            ca.delivery = 'null'
            ca.quantity = quantity

            ca.save()
            ctlr = Cart.objects.get(status='buy')

            return render(request, 'users/checkout1.html', {'message': "", 'ctlr': ctlr})


class BookingView(TemplateView):
    template_name = 'users/booking_view.html'
    def get_context_data(self, **kwargs):
        context = super(BookingView,self).get_context_data(**kwargs)
        usid=self.request.user.id
        b = Cart.objects.filter(status='paid',user_id=usid,delivery='paid')

        context['booking'] = b
        return context


class Checkout(TemplateView):
    template_name = 'users/checkout.html'

    def get_context_data(self, **kwargs):
         context = super(Checkout,self).get_context_data(**kwargs)
         # user = User.objects.get(id=self.request.user.id)

         cr = self.request.user.id
         ctr = Cart.objects.filter(status='cart',user_id=cr,delivery='null')

         total=0
         for i in ctr:
          total = total + int(i.product.price)
         print(total)

         context['ctr'] = ctr
         context['asz'] = total
         return context


    def post(self, request, *args, **kwargs):
        firstname= request.POST['firstname']
        lastname=request.POST['lastname']
        phonenumber=request.POST['phonenumber']
        email=request.POST['email']
        address=request.POST['address']

        chk = Checkout_details()
        chk.firstname=firstname
        chk.lastname=lastname
        chk.phonenumber=phonenumber
        chk.email=email
        chk.address=address
        chk.save()
        return render(request, 'users/payment1.html', {'message': ""})


class payment(TemplateView):
    def dispatch(self,request,*args,**kwargs):

        pid = self.request.user.id

        ch = Cart.objects.filter(user_id=pid,status='cart')


        print(ch)
        for i in ch:
            i.payment='paid'
            i.status='paid'
            i.delivery = 'paid'
            i.billstatus = "null"
            i.save()
        return render(request,'users/payment1.html',{'message':" payment Successfull"})
class Direct_checkout(TemplateView):
    template_name = 'users/checkout1.html'


    def post(self, request, *args, **kwargs):
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        phonenumber = request.POST['phonenumber']
        email = request.POST['email']
        address = request.POST['address']

        chk = Checkout_details()
        chk.firstname = firstname
        chk.lastname = lastname
        chk.phonenumber = phonenumber
        chk.email = email
        chk.address = address
        chk.save()
        return render(request, 'users/payment2.html', {'message': ""})


class Direct_payment(TemplateView):
    def dispatch(self,request,*args,**kwargs):

        pid = self.request.user.id

        ch = Cart.objects.filter(user_id=pid,status='buy')


        print(ch)
        for i in ch:
            i.payment='paid'
            i.status='paid'
            i.delivery = 'delivered'
            i.billstatus = "null"
            i.save()
        return render(request,'users/payment2.html',{'message':" payment Successfull"})

class My_Profile(TemplateView):
    template_name = 'users/my_profile.html'

    def get_context_data(self, **kwargs):
        context = super(My_Profile, self).get_context_data(**kwargs)
        usid = self.request.user.id

        view_cust = Customer_Reg.objects.get(user_id=usid)
        print(view_cust)

        context['view_cust'] = view_cust
        return context

    def post(self, request, *args, **kwargs):
        # fullname = request.POST['name']
        # last = request.POST['name1']

        if request.POST['profile'] == "pass":
            id = request.POST['id']
            password = request.POST['password']
            us = User.objects.get(pk=id)

            us.set_password(password)

            us.save()
        else:
            address = request.POST['address']
            id = request.POST['id']
            email = request.POST['email']
            name = request.POST['name']
            reg = Customer_Reg.objects.get(user=id)

            reg.address = address
            reg.save()
            us = User.objects.get(pk=id)
            us.username = email
            us.email = email
            us.first_name = name
            us.save()

        messages = "Update Successful."
        return render(request, 'users/my_profile.html', {'messages': "Update Successful"})
