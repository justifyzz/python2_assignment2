from django.urls import path
from . import views

# Urls of the web app
urlpatterns = [
    path('api/data', views.get_data, name='api-data'),
    path('', views.charts, name='charts-page'),
    path('api/chart/data/', views.ChartData.as_view())
]
