from django.shortcuts import render
from rest_framework.response import Response
from .models import Category
from rest_framework.views import APIView
from .serializers import CategorySerializer


class CategoryList(APIView):
    Model = Category
    serializer_class = CategorySerializer

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
