from django.urls import path
from unit.views import CountyListView, UnitList,AddUnitView


app_name = 'unit'
urlpatterns = [
    path('', CountyListView.as_view(), name='countyList'),
    path('list/<slug:county_slug>', UnitList.as_view(), name='unitList'),
    path('add_unit/', AddUnitView.as_view(), name='addUnit')

]
