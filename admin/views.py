# Create your views here.
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from admin.forms import CategoryForm
from shopCatalog.models import Category


def render_manage_category(request):
    param_map = {}
    if request.method == "POST":
        category_form = CategoryForm(request.POST)
        category_form.save()
        return HttpResponseRedirect(reverse('site_admin:manage_category'))
    else:
        param_map["category_form"] = CategoryForm()
        param_map["categories"] = Category.objects.all()
        return render(request, "admin/manage_category.html", param_map)
