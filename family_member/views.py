from django.shortcuts import render
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status
from .models import FamilyMember
from .serializers import FamilyMemberSerializer
from rest_framework.response import Response
from family_star.permissions import IsOwner
from profiles.models import Profile


class FamilyMemberList(APIView):
    """
    Views all family members

    """
    permission_classes = [IsOwner]
    serialzer_class = FamilyMemberSerializer

    def get(self, request):
        profile = Profile.objects.get(user=request.user)
        family_members = FamilyMember.objects.filter(belongs_to_profile=profile)
        serializer = FamilyMemberSerializer(family_members, many=True)
        return Response(serializer.data)

    
    def post(self, request):
        serializer = FamilyMemberSerializer(
            data=request.data, context={'request': request}
        )
        profile = Profile.objects.get(user=request.user)
        if serializer.is_valid():
            serializer.save(belongs_to_profile=profile)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class FamilyMemberDetailView(APIView):
    """
    View for displaying and update one family member.  
    """
    serializer_class = FamilyMemberSerializer
    permission_classes = [IsOwner]

    def get_object(self, pk):
        try: 
            family_member = FamilyMember.objects.get(pk=pk)
            self.check_object_permissions(self.request, family_member)
            return family_member
        except FamilyMember.DoesNotExist:
            raise Http404
    
    def get(self,request, pk):
        family_member = self.get_object(pk)
        serializer = FamilyMemberSerializer(family_member)
        return Response(serializer.data)


    def put(self, request, pk):
        family_member = self.get_object(pk)
        serializer = FamilyMemberSerializer(family_member, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        family_member = self.get_object(pk)
        family_member.delete()
        return  Response(
            status=status.HTTP_204_NO_CONTENT
        )
