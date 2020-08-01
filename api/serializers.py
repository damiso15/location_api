from rest_framework import serializers
from cities.models import City, Continent, Country, District, Region, Subregion


class ContinentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Continent
        fields = ['id', 'name', 'code']


class CountrySerializer(serializers.ModelSerializer):
    continent = serializers.CharField(source='continent.name')

    class Meta:
        model = Country
        fields = ('id', 'name', 'capital', 'code3', 'population', 'area', 'currency', 'currency_name', 'phone',
                  'currency_symbol', 'language_codes', 'continent')


class RegionSerializer(serializers.ModelSerializer):
    country = serializers.CharField(source='country.name')

    class Meta:
        model = Region
        fields = ('id', 'name', 'code', 'country')


class SubRegionSerializer(serializers.ModelSerializer):
    region = serializers.CharField(source='region.name')

    class Meta:
        model = Subregion
        fields = ('id', 'name', 'code', 'region')


class CitySerializer(serializers.ModelSerializer):
    country = serializers.CharField(source='country.name')
    region = serializers.CharField(source='region.name')

    class Meta:
        model = City
        fields = ('id', 'name', 'population', 'elevation', 'timezone', 'country', 'region')


class DistrictSerializer(serializers.ModelSerializer):
    city = serializers.CharField(source='city.name')

    class Meta:
        model = District
        fields = ('id', 'name', 'population', 'city')
