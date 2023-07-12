from django.urls import path
from .views import SnackListView,SnackDetailView


urlpatterns = [

    path('s/' ,SnackListView.as_view(), name='snack_list'),
    # path('snack_detail' ,SnackDetailView.as_view(), name='snack_detail'),
    path('s/<pk>/' ,SnackDetailView.as_view(), name='snack_detail'),
]