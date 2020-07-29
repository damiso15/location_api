from rest_framework import serializers
from cities.models import City, Continent, Country, District, Region, Subregion


class ContinentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Continent
        fields = ['id', 'name', 'code']


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'name', 'capital', 'code3', 'population', 'area', 'currency', 'currency_name', 'phone',
                  'continent')


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('id', 'name', 'code', 'country')


class SubRegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subregion
        fields = ('id', 'name', 'code', 'region')


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'name', 'population', 'elevation', 'timezone', 'country', 'region', 'subregion')


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ('id', 'name', 'population', 'city')
