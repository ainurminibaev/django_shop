# Create your views here.
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from shopCatalog.forms import GoodForm
from django.core.urlresolvers import reverse
from shopCatalog.models import Good


def index(request):
    return render(request, "mainPage.html" )

def render_catalog(request):
    param_map = {}
    param_map["goods"] = Good.objects.all()
    return render(request, "shopCatalog/catalog.html", param_map)

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
    param_map={}
    try:
           good = Good.objects.get(id=int(good_id))
    except ObjectDoesNotExist:
            good = None
    if good is None:
        return render(request, "errors/404.html")
    param_map["good"] = good
    return render(request, "shopCatalog/one_good.html", param_map)
