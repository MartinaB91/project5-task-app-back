from  django.urls import path
from .views import FamilyMemberList, FamilyMemberDetailList


urlpatterns = [
    # path('addfamilymember/', CreateFamilyMember.as_view(), name='add_family_member'),
    path('members/', FamilyMemberList.as_view()),
    path('members/<int:pk>/', FamilyMemberDetailList.as_view()),

]

