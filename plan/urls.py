from django.urls import path
from plan.views import PlanListView, DetailsPlanView,ModalAddPlanView,ChangesPlanView

app_name = 'plan'
urlpatterns = [
    path('', PlanListView.as_view(), name='planList'),
    path('details_plan/<int:planId>/', DetailsPlanView.as_view(), name='detailsPlan'),
    path('modal/', ModalAddPlanView.as_view(), name='modalAddPlan'),
    path('history_modal/<int:plan_id>/', ChangesPlanView.as_view(),name='changesPlan')

]
