from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from cms import serializers
import json



class CreateProtectionLevel(APIView):
    def post(self, request):
        body_data = json.loads(request.body.decode())
        pl_serializer = serializers.ProetctionLevelSerializer(data=body_data)
        if not pl_serializer.is_valid():
            return Response(data=pl_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        print(pl_serializer.validated_data)
        pl_serializer.create(validated_data=pl_serializer.validated_data).save()
        return Response(data={"message": "Done"}, status=status.HTTP_200_OK)
    