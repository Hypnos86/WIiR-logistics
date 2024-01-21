from django.urls import path
from plan.views import PlanListView

app_name = 'plan'
urlpatterns = [
    path('', PlanListView.as_view(), name='planList')

]
