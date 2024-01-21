from django.urls import path
from project.views import ProjectListView

app_name = 'project'
urlpatterns = [
    path('', ProjectListView.as_view(), name='projectList'),

]
