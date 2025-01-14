class ExampleService:

    def get_data(self):
        return {
            "data": "Este es un ejemplo de datos obtenidos desde el servicio."
        }

    def create_example(self, data: dict):
        # Simular guardar en una base de datos
        return {
            "id": 1,  # Simula un ID generado
            "name": data["name"],
            "age": data["age"],
            "email": data["email"]
        }