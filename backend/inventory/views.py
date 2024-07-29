from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Item, PurchaseOrder, Inventory, Supplier, IncomingItem, DepartmentInventory, Requisition
from .serializers import (
    ItemSerializer,
    PurchaseOrderSerializer,
    IncomingItemSerializer,
    InventorySerializer,
    SupplierSerializer,
    DepartmentSerializer,
    DepartmentInventorySerializer,
    RequisitionSerializer,
)

from .filters import (
    InventoryFilter,
    ItemFilter,
    PurchaseOrderFilter,
    SupplierFilter
)

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ItemFilter


# class OrderBillViewSet(viewsets.ModelViewSet):
#     queryset = OrderBill.objects.all()
#     serializer_class = OrderBillSerializer  
#     filter_backends = (DjangoFilterBackend,)
#     filterset_class = OrderBillFilter  

class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = PurchaseOrderFilter

class IncomingItemViewSet(viewsets.ModelViewSet):
    queryset = IncomingItem.objects.all()
    serializer_class = IncomingItemSerializer


class DepartmentInventoryViewSet(viewsets.ModelViewSet):
    queryset = DepartmentInventory.objects.all()
    serializer_class = DepartmentInventorySerializer

class RequisitionViewSet(viewsets.ModelViewSet):
    queryset = Requisition.objects.all()
    serializer_class = RequisitionSerializer


class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = InventoryFilter

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = SupplierFilter
