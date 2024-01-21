from django.urls import path
from donation.views import DonationListView

app_name = 'donation'
urlpatterns = [
    path('', DonationListView.as_view(), name='donationList'),

]
