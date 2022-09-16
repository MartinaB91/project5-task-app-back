from  django.urls import path
from .views import FamilyMemberList, familyMemberDetailList


urlpatterns = [
    # path('addfamilymember/', CreateFamilyMember.as_view(), name='add_family_member'),
    path('members/', FamilyMemberList.as_view()),
    path('members/<int:pk>/', familyMemberDetailList.as_view()),

]

