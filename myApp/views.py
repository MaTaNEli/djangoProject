from email import message
from wsgiref import validate
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from myApp.tests import checkInput
from myApp.models import CitizenDetails
from myApp.serializers import DepartmentSerializer

@api_view(['GET'])
def getALL(request):
    dep = CitizenDetails.objects.all()
    dep_ser = DepartmentSerializer(dep, many=True)
    return JsonResponse(dep_ser.data, safe = False)

@api_view(['GET'])
def getByCity(request):
    citizens = CitizenDetails.objects.filter(City=request.GET['city'])
    dep_ser = DepartmentSerializer(citizens, many=True)
    return JsonResponse(dep_ser.data, safe = False)

@api_view(['GET'])
def getByDOB(request):
    citizens = CitizenDetails.objects.filter(BirthDay__range=[request.GET['first'], request.GET['second']])
    dep_ser = DepartmentSerializer(citizens, many=True)
    return JsonResponse(dep_ser.data, safe = False)

@api_view(['POST'])
def addData(request):
    data1 = JSONParser().parse(request)
    message = checkInput(data1)

    if message != "":
        JsonResponse.status_code = 400
        return JsonResponse({"message": message}, safe = False)
        
    serializer = DepartmentSerializer(data = data1)
    if serializer.is_valid():
        serializer.save()
        JsonResponse.status_code = 200
        return JsonResponse({"message": "User signed in successfully"}, safe = False)
   
    JsonResponse.status_code = 400
    print(serializer.errors)
    return JsonResponse({"message": "There seems to be a problem with the program Please fill in the details again"}, safe = False)

