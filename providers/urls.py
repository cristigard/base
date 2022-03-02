from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views




urlpatterns = [
    path('', views.ServiceAreaList.as_view()),
    path('service-create/', views.ServiceAreaCreateDetail.as_view()),
    path('service/<str:coord>', views.CheckServiceArea.as_view()),
    path('service-update/<str:tk>/', views.ServiceAreaUpdateDetail.as_view()),
    path('service-delete/<str:tk>/', views.ServiceAreaDeleteDetail.as_view()),

]
urlpatterns = format_suffix_patterns(urlpatterns)
