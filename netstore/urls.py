from django.urls import path

from netstore.apps import NetstoreConfig
from netstore.views import SellerCreateApiView, SellerRetrieveApiView, SellerUpdateApiView, SellerDestroyApiView, \
    SellerListApiView

app_name = NetstoreConfig.name

urlpatterns = [
    path('seller/list/', SellerListApiView.as_view(), name='seller_list'),
    path('seller/create/', SellerCreateApiView.as_view(), name='seller_create'),
    path('seller/update/<int:pk>/', SellerUpdateApiView.as_view(), name='seller_update'),
    path('seller/retrieve/<int:pk>/', SellerRetrieveApiView.as_view(), name='seller_retrieve'),
    path('seller/delete/<int:pk>/', SellerDestroyApiView.as_view(), name='seller_delete'),

]