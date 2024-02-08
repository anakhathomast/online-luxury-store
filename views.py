from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import TemplateView

from Green_app.models import UserType, Customer_Reg,Seller_Reg


class IndexView(TemplateView):
    template_name = 'index.html'




class Users_reg(IndexView):
    template_name = 'users_reg.html'

    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        con_password = request.POST['con_password']

        address = request.POST['address']
        if password == con_password:

            if User.objects.filter(email=email):
                print('pass')
                return render(request, 'users_reg.html', {'message': "already added the email"})

            else:
                user = User.objects._create_user(username=email, password=password, email=email, first_name=name,
                                                 is_staff='0', last_name='1')
                user.save()
                customer = Customer_Reg()
                customer.user = user
                customer.address = address
                customer.con_password=con_password
                customer.save()

                usertype = UserType()

                usertype.user = user
                usertype.type = "customer"
                usertype.save()
                return render(request, 'users_reg.html', {'message': "successfully added"})
        else:
            return render(request, 'users_reg.html', {'message': "password didn't match"})

class seller_registartion(IndexView):
    template_name = 'shop_reg.html'

    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        con_password = request.POST['con_password']

        address = request.POST['address']
        if password == con_password:

            if User.objects.filter(email=email):
                print('pass')
                return render(request, 'shop_reg.html', {'message': "already added the email"})

            else:
                user = User.objects._create_user(username=email, password=password, email=email, first_name=name,
                                                 is_staff='0', last_name='0')
                user.save()
                customer = Seller_Reg()
                customer.user = user
                customer.address = address
                customer.con_password=con_password
                customer.save()

                usertype = UserType()

                usertype.user = user
                usertype.type = "shop"
                usertype.save()
                return render(request, 'shop_reg.html', {'message': "successfully added"})
        else:
            return render(request, 'shop_reg.html', {'message': "password didn't match"})


class Login1(TemplateView):
    template_name = 'login.html'

    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(username=email, password=password)

        if user is not None:
            login(request, user)
            if user.last_name == '1':
                if user.is_superuser:
                    return redirect('/admin')
                elif UserType.objects.get(user_id=user.id).type == "customer":
                    return redirect('/customer')
                elif UserType.objects.get(user_id=user.id).type == "shop":
                    return redirect('/shop')
            # elif UserType.objects.get(user_id=user.id).type == "pharmacy":
            #     return redirect('/pharmacy')

            else:
                return render(request, 'login.html', {'message': " User Account Not Authenticated"})


        else:
            return render(request, 'login.html', {'message': "Invalid Username or Password"})

