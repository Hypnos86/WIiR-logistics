from django.forms import ModelForm, DateInput
from plan.models import PlanModel


class DateField(DateInput):
    input_type = "date"


class PlanModelForm(ModelForm):
    class Meta:
        model = PlanModel
        fields = ['title', 'subtitle', 'date']
        labels = {'title': 'Tytuł', 'subtitle': 'Podtytuł', 'date': 'Data'}
        exclude = ['tasks_cost', 'create', 'change', 'author']
        widgets = {'date': DateField()}
