from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from myApp.models import CitizenDetails
from myApp.serializers import DepartmentSerializer


@api_view(['GET'])
def data(request):
    dep = CitizenDetails.objects.all()
    dep_ser = DepartmentSerializer(dep, many=True)
    return JsonResponse(dep_ser.data, safe = False)

@api_view(['POST'])
def addData(request):

    data1 = JSONParser().parse(request)
    print(data1)
    print("data")
   
    serializer = DepartmentSerializer(data = data1)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({"message": "good bro"}, safe = False)
   
    return JsonResponse({"message": "bad bro"}, safe = False)