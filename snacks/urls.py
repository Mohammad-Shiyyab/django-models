from django.urls import path
from .views import SnackListView,SnackDetailView,HomeView


urlpatterns = [

    path('s/' ,SnackListView.as_view(), name='snack_list'),
    # path('snack_detail' ,SnackDetailView.as_view(), name='snack_detail'),
    path('s/<pk>/' ,SnackDetailView.as_view(), name='snack_detail'),
    path('',HomeView.as_view(), name='home'),

]