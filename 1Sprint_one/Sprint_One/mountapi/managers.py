from .models import MountainPass, Image


class MountainPassManager:
    @staticmethod
    def submit_data(data):
        try:
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

            return {"status": 200, "message": "Отправлено успешно", "id": pass_instance.id}

        except Exception as e:
            return {"status": 500, "message": str(e), "id": None}