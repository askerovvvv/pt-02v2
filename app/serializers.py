from rest_framework import serializers

from app.models import Department, Item


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = "__all__"


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = "__all__"

    def create(self, validated_data):
        department = validated_data["department"]
        total_price = validated_data["price"] * validated_data["quantity"]

        if department.budget < total_price:
            raise serializers.ValidationError("Сумма превышает допустимы бюджет!")

        department.budget -= total_price
        department.save()
        return super().create(validated_data)


