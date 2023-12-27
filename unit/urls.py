from django.urls import path
from unit.views import UnitListView


app_name = 'unit'
urlpatterns = [
    path('list/', UnitListView.as_view(), name='unitList')

]
