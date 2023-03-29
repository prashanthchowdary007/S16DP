from .views import sample3, sample4, sample5, sample6, sample7, sample8
from django.urls import path

urlpatterns = [
    path('', sample3, name='TR'),
    path('template2/<name>/', sample4, name='CT'),
    path('template3/', sample5, name='CT'),
    path('template4/', sample6, name='LST'),
    path('redirect/', sample7, name='RD'),
    path('template5/', sample8, name='IN'),

]
