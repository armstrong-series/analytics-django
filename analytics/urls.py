from django.urls import path
from . import views

app_name = 'analytics'

urlpatterns = [
    path('incleair/dashboard/', views.Dashboard.as_view(), name='dashboard.home'),
    path('api/chart/', views.ChartData.as_view(), name='chart.analytics'),
    path('', views.Signin.as_view(), name='user.login'),
    path('data/create/', views.CreateData.as_view(), name='user.data.create')
]