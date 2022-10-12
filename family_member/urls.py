from django.urls import path
from .views import FamilyMemberList, FamilyMemberDetailView


urlpatterns = [
    path("members/", FamilyMemberList.as_view(), name="family_member_list"),
    path(
        "members/<int:pk>/",
        FamilyMemberDetailView.as_view(),
        name="family_member_detail",
    ),
]
