from shopCatalog.models import Category

def sample_context_processor(request):
    param_map = {}
    param_map['categories'] = Category.objects.all()
    param_map['cats'] = "dfdsfdsf"
    return param_map  # or whatever you want to set to variable ss