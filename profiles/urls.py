from django.urls import path
from .views import ProfileDetailList

urlpatterns = [
    path("profiles/<int:pk>/", ProfileDetailList.as_view(), name="my_profile"),
]
