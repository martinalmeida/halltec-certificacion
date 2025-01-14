from app.services.example_service import ExampleService

class ExampleController:

    def __init__(self):
        self.service = ExampleService()

    def fetch_data(self):
        data = self.service.get_data()
        return {
            "success": True,
            "message": "Datos obtenidos correctamente.",
            "payload": data,
        }

    def create_example(self, example_data: dict):
        """
        Método para manejar el procesamiento de datos del POST.
        """
        result = self.service.create_example(example_data)
        return {
            "success": True,
            "message": "Datos creados exitosamente.",
            "payload": result,
        }