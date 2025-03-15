from rest_framework.decorators import api_view
from rest_framework.response import Response

from account.models import CustomUser
from account.serializers import RegisterSerializer, UserProfileSerializer


@api_view(["POST"])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "message": "Вы прошли регистрацию, вам отправлено сообщение",
            "status": 200
        }, status=200)
    return Response(serializer.errors, status=400)


@api_view(['GET'])
def get_users(request):
    data_from_db = CustomUser.objects.all()
    department_filter_id = request.query_params.get("dep")
    if department_filter_id:
        data_from_db = data_from_db.filter(department__id=department_filter_id)
    if len(data_from_db) == 0:
        return Response({"message": "Сотрудников нету"}, status=200)

    serializer = UserProfileSerializer(data_from_db, many=True)
    return Response(serializer.data, status=200)


