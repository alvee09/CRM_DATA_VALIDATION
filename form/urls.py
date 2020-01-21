from django.urls import path

from . import views

app_name = 'form'
urlpatterns = [
    path('', views.index, name='index'),
    path('success', views.add_details, name= 'add_details'),
    path('response/<int:pk>/', views.api_response, name= 'api_response'),
    path('getSuggestions', views.getSuggestions, name= 'getSuggestions'),
    path('getAddress', views.getAddress, name= 'getAddress'),
    path('reviewed', views.reviewed, name= 'reviewed'),
    path('edit', views.edit, name= 'edit'),
    path('finalInput', views.finalInput, name= 'finalInput')
]