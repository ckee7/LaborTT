from django.urls import path

from .views import WorkInstanceListView

app_name = "work_tracker"
urlpatterns = [
    path("instances/", WorkInstanceListView.as_view(), name="instances")
]
