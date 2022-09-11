from  django.urls import path
from .views import ProfileList, ProfileDetailList

urlpatterns = [
    path('profiles/', ProfileList.as_view(), name='profiles'),
    path('profiles/<int:pk>/', ProfileDetailList.as_view(), name='my_profile'),

]