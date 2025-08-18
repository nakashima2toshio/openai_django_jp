from django.urls import path
from . import views

app_name = 'test_response_demo'

urlpatterns = [
    path('', views.index, name='index'),
    path('process/', views.process_query, name='process_query'),
    path('model/<str:model_name>/info/', views.get_model_info, name='model_info'),
]