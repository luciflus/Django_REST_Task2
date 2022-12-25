import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from django.http import JsonResponse
from rest_framework.parsers import JSONParser

from .models import Employee, Position
from .serializers import PositionSerializer, EmployeeSerializer

@csrf_exempt
def create_position(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        new_position = PositionSerializer(data=data)
        if new_position.is_valid():
            new_position.save()
            return JsonResponse(new_position.data, status=201)
        return JsonResponse(new_position.errors, status=400)
    if request.method == 'GET':
        positions = Position.objects.all()
        position_serializer = PositionSerializer(positions, many=True)
        return JsonResponse(position_serializer.data, safe=False)


@csrf_exempt
def create_employee(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        new_employee = EmployeeSerializer(data=data)
        if new_employee.is_valid():
            new_employee.save()
            return JsonResponse(new_employee.data, status=201)
        return JsonResponse(new_employee.errors, status=400)
    if request.method == 'GET':
        employees = Employee.objects.all()
        employee_serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(employee_serializer.data, safe=False)


class PositionCreateListView(generics.ListCreateAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

class EmployeeCreateListView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
