from email import message
from wsgiref import validate
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from myApp.tests import checkInput
from myApp.models import CitizenDetails
from myApp.serializers import DepartmentSerializer
from django.http import HttpResponse
import xlwt


#==================================================================================================
# The rout for expoert the data by birth dates
@api_view(['GET'])
def dateExport(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Summary.xls'
    citizens = CitizenDetails.objects.filter(BirthDay__range=[request.GET['first'], request.GET['second']])
    return exportExcel(citizens, response)

# The rout for expoert the data by city
@api_view(['GET'])
def cityExport(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Summary.xls'
    citizens = CitizenDetails.objects.filter(City=request.GET['city'])
    return exportExcel(citizens, response)

# The rout for expoert all the data
@api_view(['GET'])
def allDataExport(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Summary.xls'
    dep = CitizenDetails.objects.all()
    return exportExcel(dep, response)

#==================================================================================================
# The rout for get all the data
@api_view(['GET'])
def getALL(request):
    dep = CitizenDetails.objects.all()
    dep_ser = DepartmentSerializer(dep, many=True)
    return JsonResponse(dep_ser.data, safe = False)

# The rout for get the data filtered by city
@api_view(['GET'])
def getByCity(request):
    citizens = CitizenDetails.objects.filter(City=request.GET['city'])
    dep_ser = DepartmentSerializer(citizens, many=True)
    return JsonResponse(dep_ser.data, safe = False)

# The rout for get the data filtered by rang of dates
@api_view(['GET'])
def getByDOB(request):
    citizens = CitizenDetails.objects.filter(BirthDay__range=[request.GET['first'], request.GET['second']])
    dep_ser = DepartmentSerializer(citizens, many=True)
    return JsonResponse(dep_ser.data, safe = False)

#==================================================================================================
# The rout to save user in the DB
@api_view(['POST'])
def addData(request):
    data1 = JSONParser().parse(request)

    # validate the data from the user
    # in a case of bad data send the issue
    message = checkInput(data1)

    if message != "":
        JsonResponse.status_code = 400
        return JsonResponse({"message": message}, safe = False)

    # Put the data in the model to save in the DB   
    serializer = DepartmentSerializer(data = data1)
    if serializer.is_valid():
        serializer.save()
        JsonResponse.status_code = 200
        return JsonResponse({"message": "User signed in successfully"}, safe = False)
   
    # in any case send back 400 -> not suppose to get here
    JsonResponse.status_code = 400
    print(serializer.errors)
    return JsonResponse({"message": "There seems to be a problem with the program Please fill in the details again"}, safe = False)

#====================== Functions =====================================================
def exportExcel(data, response):
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Summary')
    row_num = 0
    
    cols =['FirstName','LastName','BirthDay','Address','City','ZipCode','LandLine','Phone','isInfected','Conditions']

    for col_num in range(len(cols)):
        ws.write(row_num,col_num,cols[col_num])

    rows = data.values_list('FirstName','LastName','BirthDay','Address','City', 
        'ZipCode','LandLine','Phone','isInfected','Conditions')
  
    for row in rows:
        row_num +=1
        for col_num in range(len(row)):
            ws.write(row_num,col_num,str(row[col_num]))

    wb.save(response)
    return response