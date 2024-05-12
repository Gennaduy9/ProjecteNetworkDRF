from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListAPIView
from rest_framework.filters import SearchFilter

from netstore.models import Seller
from netstore.permissions import IsActive
from netstore.serializers import SellerSerializer, SellerUpdateSerializer


class SellerListApiView(ListAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    permission_classes = [IsActive]
    filter_backends = [SearchFilter]
    search_fields = ['contact__country', ]
    filterset_fields = ['contact__country', ]


class SellerCreateApiView(CreateAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    permission_classes = [IsActive]


class SellerUpdateApiView(UpdateAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerUpdateSerializer
    permission_classes = [IsActive]


class SellerRetrieveApiView(RetrieveAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    permission_classes = [IsActive]


class SellerDestroyApiView(DestroyAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    permission_classes = [IsActive]
