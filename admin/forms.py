from django.forms.models import ModelForm
from shopCatalog.models import Category


class CategoryForm(ModelForm):
       class Meta:
           model = Category