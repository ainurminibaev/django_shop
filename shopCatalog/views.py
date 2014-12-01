# Create your views here.
import sys

from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Min
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse, reverse_lazy

from shopCatalog.forms import GoodForm
from shopCatalog.models import Good, Order


def index(request):
    return render(request, "mainPage.html")


def addGood(request):
    param_map = {}
    if request.method == "POST":
        good_form = GoodForm(request.POST)
        if good_form.is_valid():
            good_entity = good_form.save()
            print(good_entity)
            return HttpResponseRedirect(reverse("index"))
        else:
            param_map["good_form"] = good_form
            return render(request, "shopCatalog/addGood.html", param_map)

    elif request.method == "GET":
        param_map["good_form"] = GoodForm()
        return render(request, "shopCatalog/addGood.html", param_map)


def render_good(request, good_id):
    param_map = {}
    try:
        good = Good.objects.get(id=int(good_id))
    except ObjectDoesNotExist:
        good = None
    if good is None:
        return render(request, "errors/404.html")
    watched_goods = request.session.get("watched_goods", [])
    watched_goods.append(good.id)
    request.session["watched_goods"] = watched_goods
    param_map["good"] = good
    return render(request, "shopCatalog/one_good.html", param_map)


@login_required(login_url=reverse_lazy('login'))
def add_to_cart(request, good_id):
    try:
        good = Good.objects.get(id=int(good_id))
    except ObjectDoesNotExist:
        good = None
    if good is None or not good.isAvailable:
        return render(request, "errors/404.html")
    # find unclosed order
    try:
        order = Order.objects.get(is_purchased=False, user__id=request.user.id)
    except ObjectDoesNotExist:
        order = Order()
        order.user = request.user
        order.save()
    # TODO calc discount
    order.items.add(good)
    order.totalPrice += good.price
    order.save()
    return HttpResponseRedirect(reverse('cart'))


@login_required(login_url=reverse_lazy('login'))
def render_cart(request):
    param_map = {}
    try:
        order = Order.objects.get(is_purchased=False, user__id=request.user.id)
    except ObjectDoesNotExist:
        order = None

    param_map["order"] = order
    return render(request, "shopCatalog/cart.html", param_map)


@login_required(login_url=reverse_lazy('login'))
def delete_from_cart(request, good_id):
    good_id = int(good_id)
    try:
        order = Order.objects.get(is_purchased=False, user__id=request.user.id)
    except ObjectDoesNotExist:
        order = None
    if order:
        order.items = filter(lambda item: item.id != good_id, order.items.all())
        order.save()
    return HttpResponseRedirect(reverse('cart'))


def render_make_order(request):
    param_map = {}
    try:
        order = Order.objects.get(is_purchased=False, user__id=request.user.id)
    except ObjectDoesNotExist:
        order = None
    if (order is None):
        return HttpResponseRedirect(reverse('index'))

    param_map["order"] = order

    return render(request, "shopCatalog/make_order.html", param_map)


def make_order(request):
    if (not request.method == 'POST'):
        return HttpResponseRedirect(reverse('index'))

    param_map = {}
    try:
        order = Order.objects.get(is_purchased=False, user__id=request.user.id)
    except ObjectDoesNotExist:
        order = None
    if (order is None):
        return HttpResponseRedirect(reverse('index'))

    address = request.POST["address"]
    payment = request.POST["payment"]
    order.address = address
    order.payment_method = payment
    order.is_purchased = True
    order.save()
    param_map["order"] = order

    return render(request, "shopCatalog/success_order.html", param_map)


def filter_catalog(request):
    param_map = {}
    if (request.method == 'POST'):
        request_map = request.POST
        html_view_url = "shopCatalog/catalog_part.html"
    else:
        request_map = request.GET
        param_map["min_price"] = int((Good.objects.filter().values_list("price").annotate(Min("price"))[0])[1])
        param_map["max_price"] = int((Good.objects.filter().values_list("price").annotate(Min("price"))[0])[1])
        param_map["c_price_l"] = param_map["min_price"]
        param_map["c_price_r"] = 2 * param_map["max_price"] - param_map["max_price"] / 2
        html_view_url = "shopCatalog/catalog.html"

    try:
        category_ = int(unicode(request_map.get("catalog", None)))
    except ValueError:
        category_ = None
    try:
        min_price = int(unicode(request_map.get("min_price", -sys.maxsize - 1)))
        if request.method == 'GET' and min_price > param_map["min_price"]:
            param_map["c_price_l"] = min_price
    except ValueError:
        min_price = -sys.maxsize - 1

    try:
        max_price = int(unicode(request_map.get("max_price", sys.maxsize)))
        if request.method == 'GET' and max_price < param_map["max_price"]:
            param_map["c_price_r"] = max_price
    except ValueError:
        max_price = sys.maxsize
    try:
        page = int(unicode(request_map.get("page", 0)))
    except ValueError:
        page = 0
    if category_ and min_price:
        goods = Good.objects.filter(category__id=category_, price__range=(min_price, max_price))[page * 3:3]
    else:
        if category_ and not min_price:
            goods = Good.objects.filter(category__id=category_)[page * 3:3]
        else:
            goods = Good.objects.filter(price__range=(min_price, max_price))[page * 3:3]

    param_map["good_list"] = goods
    return render(request, html_view_url, param_map)
