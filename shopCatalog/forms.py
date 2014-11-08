from django.forms.models import ModelForm
from shopCatalog.models import Good


class GoodForm(ModelForm):

    class Meta:
        model = Good
        error_messages = {
            'name': {
                'max_length': "This good's name is too long."
            },
        }