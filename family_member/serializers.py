from rest_framework import serializers
from .models import FamilyMember
from profiles.models import Profile
# from django.contrib.auth.decorators import login_required


# @login_required
class FamilyMemberSerializer(serializers.ModelSerializer):
    belongs_to_profile = serializers.StringRelatedField(source='belongs_to_profile.user.username')
    name = serializers.CharField(max_length=200)
    #todo: Check why StringRelatedField gives KeyError when CharField work??
    # family_member_img = serializers.CharField(max_length=400)  
    family_member_img = serializers.ReadOnlyField(source='family_member_img.url')
    role = serializers.CharField(max_length=1)
    
    def create(self, validated_data):
        request = self.context.get("request")
        profile = Profile.objects.filter(user=request.user).first()  # Name is unique so it is safe to use first() to get instance instead of QuerySet     
        return FamilyMember.objects.create(
            belongs_to_profile=profile,
            name=validated_data['name'],
            family_member_img=validated_data['family_member_img'],
            role=validated_data['role']
        )

    # def get(self,request):
    #     request = self.context.get("request")
    #     profile = Profile.objects.filter(user=request.user).first()  # Name is unique so it is safe to use first() to get instance instead of QuerySet     
    #     familymembers = FamilyMember.objects.filter(belongs_to_profile=profile)
    #     print("#############################")
    #     print(profile)
    #     print("#############################")
    #     print(profile)
    #     return familymembers


    class Meta: 
        model = FamilyMember
        fields = [
            'belongs_to_profile',
            'name',
            'family_member_img',
            'role'
        ]
