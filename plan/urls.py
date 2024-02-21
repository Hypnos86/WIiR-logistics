from django.urls import path
from plan.views import PlanListView, DetailsPlanView,ModalPlanView

app_name = 'plan'
urlpatterns = [
    path('', PlanListView.as_view(), name='planList'),
    path('details_plan/<int:planId>/', DetailsPlanView.as_view(), name='detailsPlan'),
    path('modal/', ModalPlanView.as_view(), name='modalPlan')

]
