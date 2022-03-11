from django.urls import path
from .views import CollectForm
urlpatterns = [
    path("submit/", CollectForm.as_view())
]
