from django.urls import path
from unit.views import CountyListView, UnitList,AddUnitView, EditUnitView, DetailsUnitView


app_name = 'unit'
urlpatterns = [
    path('', CountyListView.as_view(), name='countyList'),
    path('list/<slug:county_slug>/', UnitList.as_view(), name='unitList'),
    path('add_unit/', AddUnitView.as_view(), name='addUnit'),
    path('edit_unit/<slug:unit_slug>/', EditUnitView.as_view(), name='editUnit'),
    path('detail_unit/<slug:unit_slug>/', DetailsUnitView.as_view(), name='detailsUnit')

]
