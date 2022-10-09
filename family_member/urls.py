from  django.urls import path
from .views import FamilyMemberList, FamilyMemberDetailList


urlpatterns = [
    # path('addfamilymember/', CreateFamilyMember.as_view(), name='add_family_member'),
    path('members/', FamilyMemberList.as_view(), name='family_member_list'),
    path('members/<int:pk>/', FamilyMemberDetailList.as_view(), name='family_member_detail'),

]

