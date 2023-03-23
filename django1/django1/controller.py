from django.db.models import Avg, Count
from django.http import JsonResponse
from .models import Cars
from .models import Brand
from .models import Customers
from .models import CarOwnership
from .serializers import CarsSerializer, CustomerDetailSerializer, BrandWithCarSerializer, StatisticFoundingSerializer
from .serializers import BrandSerializer
from .serializers import CustomerSerializer
from .serializers import CarDetailSerializer
from .serializers import BrandDetailSerializer
from .serializers import CarOwnershipSerializer
from .serializers import CarOwnershipDetailSerializer
from .serializers import StatisticSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(('GET', 'POST'))
def cars_list(request, format=None):
    #get all the cars
    #serialize them
    #return json

    if request.method == 'GET':
        cars = Cars.objects.all()
        serializer = CarsSerializer(cars, many=True)

        return Response(serializer.data)


    #if request.method == 'POST':
        #car_data = request.data
        #try:
            #new_car = Cars.objects.create(name=Brand.objects.get(name=car_data['name']),
           #                          description=car_data['description'],
          #                           engine=car_data['engine'],
         #                            type=car_data['type'],
        #                             year=car_data['year'])
       # except Brand.DoesNotExist:
      #      return Response(status=status.HTTP_404_NOT_FOUND)

     #   new_car.save()
    #    serializer = CarsSerializer(new_car)

   #     return Response(serializer.data, status=status.HTTP_201_CREATED)

    if request.method == 'POST':
        serializer = CarsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST'])
def brand_list(request, format=None):
    if request.method == 'GET':
        brands = Brand.objects.all()
        serializer = BrandSerializer(brands, many=True)

        return Response(serializer.data)

    if request.method == 'POST':
        #serializer = BrandSerializer(data=request.data)
        serializer = BrandWithCarSerializer(data=request.data)


        if serializer.is_valid():
            serializer.save()
            serializer.update_car()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(status=status.HTTP_404_NOT_FOUND)




@api_view(['GET','PUT', 'DELETE'])
def cars_detail(request,id, format=None):

    try:
        cars = Cars.objects.get(pk=id)
    except Cars.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CarDetailSerializer(cars)
        return Response(serializer.data)

    elif request.method == 'PUT':

        serializer = CarsSerializer(cars, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        cars.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','PUT', 'DELETE'])
def brand_detail(request,id, format=None):

    try:
        brands = Brand.objects.get(pk=id)
    except Brand.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BrandDetailSerializer(brands)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BrandSerializer(brands, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        brands.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def custromer_list(request, format=None):

    if request.method == 'GET':
        customers = Customers.objects.all()
        serializer = CustomerSerializer(customers, many=True)

        return Response(serializer.data)

    if request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET','PUT', 'DELETE'])
def customer_detail(request,id, format=None):

    try:
        customers = Customers.objects.get(pk=id)
    except Customers.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CustomerDetailSerializer(customers)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CustomerSerializer(customers, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        customers.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def customer_filtered(request,year, format=None):

    if request.method == 'GET':
        customers=Customers.objects.filter(year_of_birth__gt=year)
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def sale_list(request, format=None):
    if request.method == 'GET':
        sales = CarOwnership.objects.all()
        serializer = CarOwnershipSerializer(sales, many=True)

        return Response(serializer.data)

    if request.method == 'POST':
        serializer = CarOwnershipSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET','PUT', 'DELETE'])
def sales_detail(request,id, format=None):

    try:
        sales = CarOwnership.objects.get(pk=id)
    except Customers.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CarOwnershipDetailSerializer(sales)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CarOwnershipSerializer(sales, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        sales.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def statistic(request):
    statistic = Brand.objects.annotate(
        avg_production_year = Avg('cars__year'),
        car_count= Count('cars')
    ).order_by('-avg_production_year')

    serializer = StatisticSerializer(statistic, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def statisticHp(request):
    statistic = Brand.objects.annotate(
        avg_hp = Avg('cars__horsepower'),
        car_count=Count('cars')

    ).order_by('-avg_hp')

    serializer = StatisticFoundingSerializer(statistic, many=True)

    return Response(serializer.data)