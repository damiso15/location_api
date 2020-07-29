from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from cities.models import City, Continent, Country, District, Region, Subregion
from .serializers import CountrySerializer, RegionSerializer, ContinentSerializer, SubRegionSerializer, CitySerializer, \
    DistrictSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework import status

# Create your views here.


class ContinentView(APIView):

    def get(self, request):
        continent = Continent.objects.all()
        serializer = ContinentSerializer(continent, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ContinentDetailView(APIView):

    def get_object(self, slug):
        try:
            return Continent.objects.get(slug=slug)

        except Continent.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, slug):
        continent = self.get_object(slug)
        serializer = ContinentSerializer(continent)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CountryView(APIView):

    def get(self, request):
        country = Country.objects.all()
        serializer = CountrySerializer(country, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CountryDetailView(APIView):

    def get_object(self, slug):
        try:
            return Country.objects.get(slug=slug)

        except Country.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, slug):
        country = self.get_object(slug)
        serializer = CountrySerializer(country)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RegionView(APIView):

    def get(self, request):
        region = Region.objects.all()
        serializer = RegionSerializer(region, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RegionDetailView(APIView):

    def get_object(self, id):
        try:
            return Region.objects.get(id=id)

        except Region.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        region = self.get_object(id)
        serializer = RegionSerializer(region)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SubRegionView(APIView):

    def get(self, request):
        sub_region = Subregion.objects.all()
        serializer = SubRegionSerializer(sub_region, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SubRegionDetailView(APIView):

    def get_object(self, id):
        try:
            return Subregion.objects.get(id=id)

        except Subregion.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        sub_region = self.get_object(id)
        serializer = SubRegionSerializer(sub_region)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CityView(APIView):

    def get(self, request):
        city = City.objects.all()
        serializer = CitySerializer(city, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CityDetailView(APIView):

    def get_object(self, id):
        try:
            return City.objects.get(id=id)

        except City.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        city = self.get_object(id)
        serializer = CitySerializer(city)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DistrictView(APIView):

    def get(self, request):
        district = District.objects.all()
        serializer = DistrictSerializer(district, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DistrictDetailView(APIView):

    def get_object(self, id):
        try:
            return District.objects.get(id=id)

        except District.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        district = self.get_object(id)
        serializer = DistrictSerializer(district)
        return Response(serializer.data, status=status.HTTP_200_OK)
