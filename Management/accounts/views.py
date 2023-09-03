from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from .models import UserAccount 
from .serializers import UserCreateSerializer
from rest_framework import status 
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.http import Http404
from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from django.contrib.auth.models import User


class Get_Username(APIView):
    def get(self, request, format=None):
        note = UserAccount.objects.all()
        serializer = UserCreateSerializer(note, many=True)
        return Response(serializer.data)

