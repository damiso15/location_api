from django.urls import path
from .views import CountryView, RegionView, ContinentView, SubRegionView, CityView, DistrictView, ContinentDetailView, \
    CountryDetailView, RegionDetailView, SubRegionDetailView, CityDetailView, DistrictDetailView


urlpatterns = [
    path('continent/', ContinentView.as_view()),
    path('continent/<slug:slug>/', ContinentDetailView.as_view()),
    path('country/', CountryView.as_view()),
    path('country/<slug:slug>/', CountryDetailView.as_view()),
    path('region/', RegionView.as_view()),
    path('region/<int:id>/', RegionDetailView.as_view()),
    path('subregion/', SubRegionView.as_view()),
    path('subregion/<int:id>/', SubRegionDetailView.as_view()),
    path('city/', CityView.as_view()),
    path('city/<int:id>/', CityDetailView.as_view()),
    path('district/', DistrictView.as_view()),
    path('district/<int:id>/', DistrictDetailView.as_view()),
]
