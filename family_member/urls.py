from  django.urls import path
from .views import FamilyMemberList, familyMemberDetailList


urlpatterns = [
    # path('addfamilymember/', CreateFamilyMember.as_view(), name='add_family_member'),
    path('familymembers/', FamilyMemberList.as_view()),
    path('familymembers/<int:pk>/', familyMemberDetailList.as_view()),

]