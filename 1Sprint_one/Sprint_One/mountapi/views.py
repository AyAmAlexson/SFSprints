from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .managers import MountainPassManager
from .serializers import MountainPassSerializer
from .models import *


class SubmitDataView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        result = MountainPassManager.submit_data(data, request)

        if result["status"] == 200:
            return Response(result, status=status.HTTP_200_OK)

        return Response(result, status=result["status"])