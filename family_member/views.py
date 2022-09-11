from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from .models import FamilyMember
from .serializers import FamilyMemberSerializer

class FamilyMemberList(generics.ListCreateAPIView):
    queryset = FamilyMember.objects.all()
    serializer_class = FamilyMemberSerializer
