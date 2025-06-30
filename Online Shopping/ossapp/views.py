from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from . models import Product, Category, Customer



def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')

def productPage(request):
    category_id=request.GET.get('category')
    data = {}
    if category_id:
        products= Product.get_products_by_categoryid(category_id)
    else:
        products = Product.get_all_products()
    category = Category.get_all_category()
    data['products'] = products
    data['category'] = category
    return render(request, 'product.html', data)


def register(request):
    if request.method == 'POST':
        err=None
        name= request.POST.get('name')
        email = request.POST.get('email')
        passwd = request.POST.get('password')
        addr = request.POST.get('address')
        pin = request.POST.get('pincode')
        phone = request.POST.get('phone')
        gen = request.POST.get('gender')

        #Validation
        values={'name':name,
                'email':email,
                'addr':addr,
                'pin':pin,
                'phone':phone,
                'gen':gen,}
        customer = Customer(name=name, gender=gen, address=addr, pincode=pin, contactno=phone, emailaddress=email,
                            password=passwd)
        if not name.isalpha():
            err="Invalid Name, please try again"
        if not phone.isnumeric() or len(phone)<10:
            err="Invalid Contact Number, please try again"
        if not pin.isnumeric():
            err="Invalid Pincode, please try again"
        if customer.is_exists():
            err="Email Already Exists"
        data={}
        data['err']=err
        data['values']=values
        if err:
            return render(request, 'register.html',data)
        #customer.password=make_password(passwd)
        customer.save()
        err = "You are registered! Try Logging in"
        return render(request, 'login.html',{'err':err})
    else:
        return render(request, 'register.html')

def login(request):
    return render(request,'login.html')


def user(request):
    return render(request,'user.html')

def orders(request):
    return render(request,'orders.html')