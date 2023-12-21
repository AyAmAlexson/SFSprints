from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .managers import MountainPassManager
from .serializers import MountainPassSerializer
from .models import *


class SubmitDataView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        result = MountainPassManager.submit_data(data)

        if result["status"] == 200:
            pass_instance = MountainPass.objects.get(id=result["id"])
            serializer = MountainPassSerializer(pass_instance)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response({"message": result["message"]}, status=result["status"])
