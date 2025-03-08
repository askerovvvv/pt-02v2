from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet

from app.models import Department, Item
from app.serializers import DepartmentSerializer, ItemSerializer


# Create your views here.
class DepartmentModelViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class ItemViewSet(ViewSet):

    def list(self, request):
        data = Item.objects.all()
        serializer = ItemSerializer(data, many=True)
        return Response({
            "count": len(serializer.data),
            "status": 200,
            "items": serializer.data
        }, status=200)

    def create(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            data["total_price"] = data["price"] * data["quantity"]
            return Response({
                "status": "CREATED",
                "created_item": data,
            })
        return Response(serializer.errors, status=400)


