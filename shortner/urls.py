from django.urls import path, re_path
from .views import UrlShortnerView, UrlAnalyticsView, UrlUpdateView, UrlRedirectView

urlpatterns = [
    path("urls/", UrlShortnerView.as_view(), name="url-view"),
    path("urls/<int:id>/", UrlUpdateView.as_view(), name="url-update"),
    path("analytics/", UrlAnalyticsView.as_view(), name="url-analytics"),
    path("<str:slug>/stats/", UrlAnalyticsView.as_view(), name="url-analytics"),
    re_path(r'^(?P<slug>[a-zA-Z0-7]{8})/$', UrlRedirectView.as_view(), name="url-redirect-view"),
]