from django.urls import path, include

from .views import *

urlpatterns = [

   path('', ProductsList.as_view()),
   path('<int:pk>', ProductDetail.as_view()),
   path('news/', NewsList.as_view()),
   path('news/<int:pk>', NewsDetail.as_view()),
   path('pages/', include('django.contrib.flatpages.urls')),
]