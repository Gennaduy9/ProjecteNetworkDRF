from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListAPIView
from rest_framework.filters import SearchFilter

from netstore.models import Seller
from netstore.permissions import IsActive
from netstore.serializers import SellerSerializer, SellerUpdateSerializer


class SellerListApiView(ListAPIView):
    """
    Представление для получения списка объектов сети продавцов.
    Позволяет получить список всех объектов сети продавцов с возможностью фильтрации и поиска.
    """
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    permission_classes = [IsActive]
    filter_backends = [SearchFilter]
    search_fields = ['contact__country', ]
    filterset_fields = ['contact__country', ]


class SellerCreateApiView(CreateAPIView):
    """
    Представление для создания нового объекта сети продавцов.
    Позволяет создать новый объект сети продавцов.
    """
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    permission_classes = [IsActive]


class SellerUpdateApiView(UpdateAPIView):
    """
    Представление для обновления существующего объекта сети продавцов.
    Позволяет обновить существующий объект сети продавцов по его идентификатору.
    """
    queryset = Seller.objects.all()
    serializer_class = SellerUpdateSerializer
    permission_classes = [IsActive]


class SellerRetrieveApiView(RetrieveAPIView):
    """
    Представление для получения информации о конкретном объекте сети продавцов.
    Позволяет получить информацию о конкретном объекте сети продавцов по его идентификатору.
    """
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    permission_classes = [IsActive]


class SellerDestroyApiView(DestroyAPIView):
    """
    Представление для удаления существующего объекта сети продавцов.
    Позволяет удалить существующий объект сети продавцов по его идентификатору.
    """
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    permission_classes = [IsActive]
