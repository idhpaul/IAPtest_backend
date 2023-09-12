from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns

from IAP import views

urlpatterns = [

    path('purchace/', views.PurchaceList.as_view()),
    path('purchace/<int:pk>/', views.PurchaceDetail.as_view()),
    path('user/', views.UserList.as_view()),
    path('user/<int:pk>/', views.UserDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)