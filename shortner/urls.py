from django.urls import path
from .views import UrlShortnerView, UrlAnalyticsView, UrlUpdateView

urlpatterns = [
    path("urls/", UrlShortnerView.as_view(), name="url-view"),
    path("urls/<int:id>/", UrlUpdateView.as_view(), name="url-update"),
    path("analytics/", UrlAnalyticsView.as_view(), name="url-analytics")
]