from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views 



urlpatterns = [
    path('register/', views.register, name = 'register'),
    path('login/', views.UserLoginView.as_view(), name = 'login'),
    path('logout/', views.UserLogoutView.as_view(), name = 'logout'),

    path('provider-create/', views.ProviderCreateDetail.as_view()),
    path('providers/', views.ProvidersList.as_view()),
    path('provider-retrive/<str:tk>/', views.ProviderRetriveDetail.as_view()),
    path('provider-update/<str:tk>/', views.ProviderUpdateDetail.as_view()),
    path('provider-delete/<str:tk>/', views.ProviderDeleteDetail.as_view()),

    
] 

urlpatterns = format_suffix_patterns(urlpatterns)