from django.shortcuts import render
from rest_framework.response import Response

# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from api.models import *
from api.serializers import *
from rest_framework import status
from rest_framework.permissions import IsAuthenticated



@api_view()
@permission_classes([IsAuthenticated])
def StudentJData(request):
    SQS = Student.objects.all()
    SJD = StudentModelSerializer(SQS, many=True)
    return Response(SJD.data)