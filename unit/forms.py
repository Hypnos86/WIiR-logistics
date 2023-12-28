from django.forms import ModelForm, Textarea, widgets
from unit.models import Unit


class UnitForm(ModelForm):
    class Meta:
        model = Unit
        fields = ('county', 'type', 'address', 'zip_code', 'city', 'full_name',
                  'manager', 'status', 'slug', 'information', 'change', 'author')
        exclude = ['unit_full_name', 'slug', 'change', 'author']
        labels = {'county': 'Powiat',
                  'type': 'Rodzaj jednostki',
                  'address': 'Adres',
                  'zip_code': 'Kod pocztowy',
                  'city': 'Miasto',
                  'full_name': 'Nazwa obiektu',
                  'manager': 'Administrator obiektu',
                  'status': 'Status jednostki',
                  'information': 'Informacje',
                  'create': 'Utworzenie',
                  'change': 'Zmiany',
                  'author': 'Autor'
                  }
        widgets = {'information': Textarea(attrs={'rows': 3}),
                   'zip_code': widgets.TextInput(attrs={'pattern': '^[0-9]{2}-[0-9]{3}$', 'placeholder': '00-000'}),
                   }
