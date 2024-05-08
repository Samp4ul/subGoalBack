# myapp/urls.py

from django.urls import path
from .views import verify, modify_point, add_subgoal, get_data

urlpatterns = [
    path('verify/', verify, name='verify'),
    path('modify_point/', modify_point, name='modify_point'),
    path('add_subgoal/', add_subgoal, name='add_subgoal'),
    path('get_data/', get_data, name='get_data'),
]
