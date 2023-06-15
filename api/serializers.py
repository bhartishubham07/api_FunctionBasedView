from rest_framework import serializers

from api.models import *

class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        #fields = ['Name','Roll','City']