from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from vindecoder.models import Car
from vindecoder.serializers import CarSerializer


def car_list(request):
    if request.method == 'GET':
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return JsonResponse(serializer.data, safe=False)


def car_certain(request, key):
    try:
        # car = Car.objects.get(pk=pk.upper())
        car = Car.objects.filter(wmi=key.upper())
    except Car.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CarSerializer(car, many=True)
        return JsonResponse(serializer.data, safe=False)
