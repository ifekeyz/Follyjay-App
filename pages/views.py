from django.shortcuts import get_object_or_404, render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.contrib.auth import logout as auth_logout
from django.http import JsonResponse
import json
from django.contrib.auth import login, logout

from .models import Product,Cart,Cartitems,Customer


# Create your views here.
def index(request):
    beauty_healths = Product.objects.filter(product_item='Beauty_Health')[:4]
    confectionary = Product.objects.filter(product_item='Confectioneries')[:4]
    drinks = Product.objects.filter(product_item='Drinks')[:4]
    grain_flours = Product.objects.filter(product_item='Grain_Flour')[:4]
    meat_vegetables = Product.objects.filter(product_item='Meat_vegetable')[:4]
    species_oil = Product.objects.filter(product_item='Species_oil')[:4]
    tubers = Product.objects.filter(product_item='Tuber')[:4]
    untensiles = Product.objects.filter(product_item='Untensiles')[:4]

    # if request.user.is_authenticated:
    #     customer = request.user.customer
    #     cart, created = Cart.objects.get_or_create(customer = customer, completed = False)
    #     cartitems = cart.cartitems_set.all()

    context = {
        'beauty_healths':beauty_healths,
        'confectionary':confectionary,
        'drinks':drinks,
        'grain_flours':grain_flours,
        'meat_vegetables':meat_vegetables,
        'species_oil':species_oil,
        'tubers':tubers,
        'untensiles':untensiles,
        # 'cart':cart
    }


    return render(request, 'screens/index.html',context)

def beauty_health_page(request):
    beauty_healths = Product.objects.filter(product_item='Beauty_Health')

    if request.user.is_authenticated:
        customer = request.user.customer
        cart, created = Cart.objects.get_or_create(customer = customer, completed = False)
        cartitems = cart.cartitems_set.all()
    else:
        cartitems = []
        cart = {"get_cart_total": 0, "get_itemtotal": 0}


    context={
        'beauty_healths':beauty_healths,
        'cart':cart
    }
    return render(request, 'screens/beauty_health/beauty_health.html',context)

def beauty(request, beauty_id):
    beautys =Product.objects.filter(product_item='Beauty_Health')
    beauty = get_object_or_404(beautys, pk=beauty_id)
    

    context = {
        'beauty':beauty,
        'beautys':beautys
    }
    return render(request, 'screens/beauty_health/single_beauty_health.html',context)


def confectioneries_page(request):
    confectioneries = Product.objects.filter(product_item='Confectioneries')

    if request.user.is_authenticated:
        customer = request.user.customer
        cart, created = Cart.objects.get_or_create(customer = customer, completed = False)
        cartitems = cart.cartitems_set.all()
    else:
        cartitems = []
        cart = {"get_cart_total": 0, "get_itemtotal": 0}


    context={
        'confectioneries':confectioneries,
        'cart':cart
    }
    return render(request, 'screens/confentioneries/confentioneries.html',context)

def confectionerie(request, confectionerie_id):
    confectioneries =Product.objects.filter(product_item='Confectioneries')
    confectionerie = get_object_or_404(confectioneries, pk=confectionerie_id)
    

    context = {
        'confectionerie':confectionerie,
        'confectioneries':confectioneries
    }
    return render(request, 'screens/confentioneries/single_confentioneries.html',context)

def drinks_page(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        cart, created = Cart.objects.get_or_create(customer = customer, completed = False)
        cartitems = cart.cartitems_set.all()
    else:
        cartitems = []
        cart = {"get_cart_total": 0, "get_itemtotal": 0}
    drinks =Product.objects.filter(product_item='Drinks')


    context={
        'drinks':drinks,
        'cart':cart
    }
    return render(request, 'screens/drinks/drinks.html',context)


def drink(request, drink_id):
    drinks =Product.objects.filter(product_item='Drinks')
    drink = get_object_or_404(drinks, pk=drink_id)
    

    context = {
        'drink':drink,
        'drinks':drinks
    }
    return render(request, 'screens/drinks/single_drinks.html',context)


def grain_flour_page(request):
    grain_flours =Product.objects.filter(product_item='Grain_Flour')

    if request.user.is_authenticated:
        customer = request.user.customer
        cart, created = Cart.objects.get_or_create(customer = customer, completed = False)
        cartitems = cart.cartitems_set.all()
    else:
        cartitems = []
        cart = {"get_cart_total": 0, "get_itemtotal": 0}
    
    context={
        'grain_flours':grain_flours,
        'cart':cart
    }
    return render(request, 'screens/grain_flour/grain_flour.html',context)


def grain(request, grain_id):
    grains =Product.objects.filter(product_item='Grain_Flour')
    grain = get_object_or_404(grains, pk=grain_id)
    

    context = {
        'grains':grains,
        'grain':grain
    }
    return render(request, 'screens/grain_flour/single_grain_flour.html',context)


def meat_vegetable_page(request):
    meat_vegetables =Product.objects.filter(product_item='Meat_vegetable')

    if request.user.is_authenticated:
        customer = request.user.customer
        cart, created = Cart.objects.get_or_create(customer = customer, completed = False)
        cartitems = cart.cartitems_set.all()
    else:
        cartitems = []
        cart = {"get_cart_total": 0, "get_itemtotal": 0}

    context={
        'meat_vegetables':meat_vegetables,
        'cart':cart
    }
    return render(request, 'screens/meat_vegetable/meat_vegetable.html',context)


def meat(request, meat_id):
    meats =Product.objects.filter(product_item='Meat_vegetable')
    meat = get_object_or_404(meats, pk=meat_id)
    

    context = {
        'meats':meats,
        'meat':meat
    }
    return render(request, 'screens/meat_vegetable/single_meat_vegetable.html',context)

def species_oil_page(request):
    species_oils =Product.objects.filter(product_item='Species_oil')

    if request.user.is_authenticated:
        customer = request.user.customer
        cart, created = Cart.objects.get_or_create(customer = customer, completed = False)
        cartitems = cart.cartitems_set.all()
    else:
        cartitems = []
        cart = {"get_cart_total": 0, "get_itemtotal": 0}

    context={
        'species_oils':species_oils,
        'cart':cart
    }
    return render(request, 'screens/species_oil/species_oil.html',context)


def oil(request, oil_id):
    oils =Product.objects.filter(product_item='Species_oil')
    oil = get_object_or_404(oils, pk=oil_id)
    

    context = {
        'oils':oils,
        'oil':oil
    }
    return render(request, 'screens/species_oil/single_species_oil.html',context)


def tuber_page(request):
    tubers =Product.objects.filter(product_item='Tuber')

    if request.user.is_authenticated:
        customer = request.user.customer
        cart, created = Cart.objects.get_or_create(customer = customer, completed = False)
        cartitems = cart.cartitems_set.all()
    else:
        cartitems = []
        cart = {"get_cart_total": 0, "get_itemtotal": 0}


    context={
        'tubers':tubers,
        'cart':cart
    }
    return render(request, 'screens/tuber/tuber.html',context)

def tuber(request, tuber_id):
    tubers =Product.objects.filter(product_item='Tuber')
    tuber = get_object_or_404(tubers, pk=tuber_id)
    

    context = {
        'tubers':tubers,
        'tuber':tuber
    }
    return render(request, 'screens/tuber/single_tuber.html',context)

def untensils_page(request):
    untensiles = Product.objects.filter(product_item='Untensiles')

 
        
    if request.user.is_authenticated:
        customer = request.user.customer
        cart, created = Cart.objects.get_or_create(customer = customer, completed = False)
        cartitems = cart.cartitems_set.all()

    else:
        cartitems = []
        cart = {"get_cart_total": 0, "get_itemtotal": 0}

    context={
        'untensiles':untensiles,
        'cart':cart
    }

    
    return render(request, 'screens/utensiles/utensiles.html',context)


def africa(request, africa_id):
    africas =Product.objects.filter(product_item='Untensiles')
    africa = get_object_or_404(africas, pk=africa_id)
    

    context = {
        'africas':africas,
        'africa':africa
    }
    return render(request, 'screens/utensiles/single_utensiles.html',context)


def register_login(request):
    
    if request.method == 'POST':
        # Get from values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # check if passwords match
        if password == password2:
           
            # check Username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register_login')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is been used')
                    return redirect('register_login')
                else:
                    # return

       
                    user = User.objects.create_user(username=username, password=password, email=email,
                    first_name=first_name, last_name=last_name)
                    # Login after register
                    # auth.login(request, user)
                    # messages.success(request, 'You re now logged in')
                    # return redirect('index')

                    user.save()
                    messages.success(request, 'you are now registered and can log in')
                    return redirect('login')

        else:
            messages.error(request, 'passwords do not match')
            return redirect('register_login')  
    else:
        return render(request, 'screens/register_login.html')
    

def login(request):
    if request.method == 'POST':
          # Login User
          username = request.POST['username']
          password = request.POST['password']

          user = auth.authenticate(username=username,password=password)

          if user is not None:
              auth.login(request, user)
              messages.success(request, 'you are now logged in')
              return redirect('index')
       
          else:
              messages.error(request, 'Invalid credentials')
              return redirect('login')
    else:
        return render(request, 'screens/login.html')


def logout(request):
    auth_logout(request)
    messages.success(request, 'you are now logged out..... Session expired')
    return redirect('login')


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        cart, created = Cart.objects.get_or_create(customer = customer, completed = False)
        cartitems = cart.cartitems_set.all()
    else:
        cartitems = []
        cart = {"get_cart_total": 0, "get_itemtotal": 0}

    return render(request, 'screens/cart.html', {
        'cartitems' : cartitems,
        'cart':cart
        })


def updateCart(request):
    data = json.loads(request.body)
    productId = data["productId"]
    action = data["action"]
    product = Product.objects.get(id=productId)
    customer = request.user.customer
    cart, created = Cart.objects.get_or_create(customer = customer, completed = False)
    cartitem, created = Cartitems.objects.get_or_create(cart = cart, product=product)

    if action == "add":
        cartitem.quantity += 1
        cartitem.save()
    return JsonResponse("Cart Updated", safe=False)

def updateQuantity(request):
    data = json.loads(request.body)
    quantityFieldValue = data['qfv']
    quantityFieldProduct = data['qfp']
    product = Cartitems.objects.filter(product__name = quantityFieldProduct).last()
    product.quantity = quantityFieldValue
    product.save()
    return JsonResponse("Quantity Updated", safe=False)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        cart, created = Cart.objects.get_or_create(customer = customer, completed = False)
        cartitems = cart.cartitems_set.all()
    return render(request, 'screens/checkout.html',{
        'cartitems' : cartitems,
        'cart':cart }
    )



def order(request):
    return render(request, 'screens/order_page.html')
