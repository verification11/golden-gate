from django.urls import path
from .views import index, housing, about

urlpatterns = [
    path('', index, name='index' ),
    path('housing', housing, name='buying' ),
    path('about-us', about, name='about')
]
