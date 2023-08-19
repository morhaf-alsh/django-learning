from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import render
from parkManage.models import Car
from parkManage.serializer import CarSerializer
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

@api_view(['GET'])
def currentList(request):
    # data = Car.objects.all().order_by('brand')
    # context = {
    #     'data' : data
    # }
    # return render(request, 'list.html', context)
    raw_data = Car.objects.all()
    serializer = CarSerializer(raw_data,many=True)
    return Response(serializer.data)

@api_view(['GET','PUT','DELETE'])
def car_info(request,id):
    # if request.
    # # context = {
    # #     'data' : data
    # # }
    # return render(request, 'list.html', context)
    try:
        raw_data = Car.objects.get(pk=id)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CarSerializer(raw_data)
        return Response(serializer.data,status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = CarSerializer(raw_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        raw_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def create(request):

    serializer = CarSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
