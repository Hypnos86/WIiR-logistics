from django.urls import path
from contract.views import ContractListView

app_name = 'contract'
urlpatterns = [
    path('', ContractListView.as_view(), name='contractList'),
]
