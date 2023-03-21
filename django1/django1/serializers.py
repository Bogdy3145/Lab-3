from rest_framework import serializers
from .models import Cars
from .models import Brand
from .models import Customers
from .models import CarOwnership

class CarsSerializer(serializers.ModelSerializer):

    #id = serializers.IntegerField(write_only=True)
    #name = serializers.CharField(max_length=255)
    name = serializers.SlugRelatedField(queryset=Brand.objects.all(),slug_field='name')

    description = serializers.CharField(max_length=255)
    engine = serializers.CharField(read_only=True)
    type = serializers.CharField(read_only=True)
    year = serializers.IntegerField(read_only=True)


    def validate_brand_id(self, value):
        filter = Brand.objects.filter(id=value)
        if not filter.exists():
            raise serializers.ValidationError("Brand does not exist")
        return value

    class Meta:
        model = Cars
        fields = ['id', 'name', 'description', 'engine', 'type', 'year']


class CarDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = ['id', 'name', 'description', 'engine', 'type', 'year']
        depth=1


class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = ['id', 'name', 'founding_year', 'owner_name', 'rarity', 'hq_address']


class BrandDetailSerializer(serializers.ModelSerializer):
    cars = CarsSerializer(many=True, read_only=True)

    class Meta:
        model = Brand
        fields = ['id', 'name', 'founding_year', 'owner_name', 'rarity', 'hq_address', 'cars']


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customers
        fields = ['id', 'name', 'year_of_birth', 'address','gender', 'phone']


class CustomerDetailSerializer(serializers.ModelSerializer):
    cars_sold = serializers.SerializerMethodField()

    class Meta:
        model = Customers
        fields = ['id', 'name', 'year_of_birth', 'address','gender', 'phone', 'cars_sold']

    def get_cars_sold(self,obj):

        cars_sold = CarOwnership.objects.filter(customer_id=obj)
        return CarOwnershipSerializer(cars_sold, many=True).data


class CarOwnershipSerializer(serializers.ModelSerializer):
    car_id = serializers.SlugRelatedField(queryset=Cars.objects.all(), slug_field='id')
    customer_id = serializers.SlugRelatedField(queryset=Customers.objects.all(), slug_field='name')
    date = serializers.DateField()
    name_of_dealer = serializers.CharField(max_length=200, default="0")

    class Meta:
        model = CarOwnership
        fields = ['id', 'car_id', 'customer_id', 'date', 'name_of_dealer']


class CarOwnershipDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarOwnership
        fields = ['id', 'car_id', 'customer_id', 'date', 'name_of_dealer']
        depth=1


class StatisticSerializer(serializers.ModelSerializer):
    avg_production_year = serializers.IntegerField(read_only=True)
    car_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Brand
        fields = ['id', 'name', 'avg_production_year', 'car_count']
