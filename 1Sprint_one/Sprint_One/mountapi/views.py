from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .managers import MountainPassManager
from .serializers import MountainPassSerializer
from .models import *
import json

class SubmitDataView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body.decode('utf-8'))
            user_id = data.get('user_id')

            if not user_id:
                return Response({'status': 400, 'message': 'Bad Request', 'id': None}, status=status.HTTP_400_BAD_REQUEST)

            result = MountainPassManager.submit_data(data, user_id)
            return Response(result, status=status.HTTP_200_OK)

        except json.JSONDecodeError:
            return Response({'status': 400, 'message': 'Bad Request', 'id': None}, status=status.HTTP_400_BAD_REQUEST)