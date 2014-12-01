from django.core.exceptions import ObjectDoesNotExist

from shopCatalog.models import Category, City


def sample_context_processor(request):
    param_map = {}
    param_map['categories'] = Category.objects.all()
    param_map['cities'] = City.objects.all()
    try:
        param_map['a_city'] = City.objects.get(id=request.COOKIES.get('city', '-100'))
    except ObjectDoesNotExist:
        pass
    return param_map