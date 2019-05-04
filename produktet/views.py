from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.checks import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.

from produktet.models import Produkte, Kategorite, AddToCart, Commentsection

# product select
def browse(request):
    if request.method =='GET':
        kat = Kategorite.objects.all()
        produkt = Produkte.objects.all()
        paginator = Paginator(produkt, 9)
        page = request.GET.get('page', 1)
        try:
            prod = paginator.page(page)
        except PageNotAnInteger:
            prod = paginator.page(1)
        except EmptyPage:
            prod = paginator.page(paginator.num_pages)
        return render(request, 'browse.html', {'products': prod, 'kategorite': kat})


# kategoty select by id
def filter(request):
    kat = request.GET['kat']
    produktet = Produkte.objects.filter(kategori_id = kat)
    kat = Kategorite.objects.all()
    return render(request, 'browse.html', {'products': produktet,'kategorite': kat})

# user login
def login_method(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            print("loged in")
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/restaurant/')
            else:
                print("user is disabled")
                return HttpResponse('Your account is disabled.')
        else:
            return HttpResponseRedirect('/login/')
    else:
        return render(request, 'login.html')

#user register
def register_method(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        password = request.POST['password']
        email = request.POST['email']
        if User.objects.filter(email = email).exists():
            print("user already exists !")
        else:
            user = User.objects.create_user(email, email, password)
            user.first_name = first_name
            user.save()
            return render(request, 'login.html')
    return render(request, 'register.html')

# return to main page
def home_page(request):
    if request.method == 'GET':
        return render(request, 'Restaurant.html')
    else:
        return render(request, 'register.html')

#buy now
def buy_now(request):
    if request.method == 'GET':
        quantity = 1
        produkt_id = request.GET['id']
        if request.user.is_authenticated:
            purchuase = AddToCart(quantity = quantity, id_user = request.user, id_product = Produkte.objects.get(id = produkt_id))
            purchuase.save()
        else:
            print('User not authenticated!')
    return HttpResponseRedirect('/browse/')

#purchuases
def purchuases(request):
    if request.method =='GET':
        cart = AddToCart.objects.filter(id_user = request.user, orderd = False)
        shuma = 0
        for sh in cart:
            shuma = sh.cmimi_total + shuma

        a = {
            'purchuase': cart,
            'shuma': shuma
        }
        return render(request, 'cart.html', a)

#delete
def delete(request):
    if request.method == 'GET':
        prod_delete = AddToCart.objects.get(id = request.GET['id'])
        prod_delete.delete()
        return HttpResponseRedirect('/cart/')

#check out
def check_out(request):
    if request.method == 'GET':
        checked = AddToCart.objects.filter(id_user = request.user, orderd = False)
        for a in checked:
            a.orderd = True
            a.save()
        return HttpResponseRedirect('/browse/')

#delivery points
# def delivery_points(request):
#     if request.method == 'GET':
#         blerjet = AddToCart.objects.filter(id_user = request.user)
#         blerjet.save()

#logout
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/restaurant/')

#search
def search(request):
    if request.method == 'POST':
        var = request.POST['text1']
        kat = Kategorite.objects.all()
        if var:
            var1 = Produkte.objects.filter(emri__icontains = var)
            if var1:
                return  render(request, 'Browse.html', {'kerkimi':var1, 'kategorite':kat})
            else:
                messages.Error(request, 'no result found')
        else:
            return HttpResponseRedirect('/restaurant/')

    return render(request, 'Browse.html')

#about us
# def commentsection(request):
# #     if request.method == 'GET':
# #         thecomment = request.POST['coment']
# #         if request.user.is_authenticated:
# #             c = Commentsection.objects.create(comment = thecomment, user_id = request.user.id)
# #             c.save()
# #             return render(request, 'About.html')
# #         else:
# #             return HttpResponseRedirect('/login/')
# #     else:
# #         if request.method =='POST':
# #             coments = Commentsection.objects.all()
# #             return render(request, 'About.html', {'komentet': coments})

def aboutus(request):
    if request.method =='GET':
        return render(request, 'About.html')