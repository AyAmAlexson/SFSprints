from .models import MountainPass, Image
from rest_framework.request import Request as DRFRequest
from .serializers import MountainPassSerializer

class MountainPassManager:
    @staticmethod
    def submit_data(data, request=None):
        try:
            # Ваш код для добавления данных в базу
            pass_instance = MountainPass.objects.create(
                beauty_title=data["beauty_title"],
                title=data["title"],
                other_titles=data["other_titles"],
                connect=data["connect"],
                add_time=data["add_time"],
                user=data["user"],
                coord=data["coords"],
                level=data["level"]
            )

            for image_data in data["images"]:
                Image.objects.create(
                    mountain_pass=pass_instance,
                    data=image_data["data"],
                    title=image_data["title"]
                )

            # Передайте запрос в контексте при создании экземпляра сериализатора
            if request and isinstance(request, DRFRequest):
                context = {'request': request}
            else:
                context = {}

            serializer = MountainPassSerializer(pass_instance, context=context)

            return {"status": 200, "message": "Отправлено успешно", "id": pass_instance.id}

        except Exception as e:
            return {"status": 500, "message": str(e), "id": None}
