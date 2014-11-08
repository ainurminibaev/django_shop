from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render

from shopCatalog.models import Good


def no_auth_please(v):
    def wrapper(request, *a, **k):
        user = request.user
        if user.is_authenticated():
            return HttpResponseRedirect(reverse("index"))
        else:
            return v(request, *a, **k)

    return wrapper


@login_required(login_url=reverse_lazy("login"))
def sign_out(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))


@no_auth_please
def sign_in(request):
    param_map = {}
    if request.POST:
        user = authenticate(
            username=request.POST["login"],
            password=request.POST["password"]
        )
        if user:
            login(request, user)
            if request.GET.has_key("next"):
                return HttpResponseRedirect(request.GET["next"])
            else:
                return HttpResponseRedirect(reverse('index'))
        else:
            return HttpResponseRedirect(reverse('login'))
    else:
        if request.GET.has_key("next"):
            param_map["next"] = request.GET["next"]
        return render(request, "users/login.html", param_map)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect(reverse('login'))
    else:
        form = UserCreationForm()
    return render(request, "users/register.html", {
        'form': form,
    })


def render_watched(request):
    param_map = {}
    watched_good_ids = request.session.get("watched_goods", [])
    goods_list = Good.objects.filter(pk__in=watched_good_ids)
    param_map["goods"] = goods_list
    return render(request, "users/watched_goods.html", param_map)