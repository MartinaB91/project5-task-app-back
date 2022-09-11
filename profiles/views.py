from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view, renderer_classes
from rest_framework import authentication, permissions
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer



class ProfileList(APIView):
    """
    Views all profiles. Only Admin have this premission.
    """
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)


class ProfileDetailList(APIView):
    serializer_class = ProfileSerializer

    def get(self,request):
        profile = Profile.objects.get()
        self.check_object_permissions(self.request, profile)
        return profile

