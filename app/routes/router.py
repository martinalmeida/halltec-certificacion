from fastapi import APIRouter
from app.controllers.example_controller import ExampleController
from app.schemas.example_schema import ExampleDTO

class ExampleRouter:
    """
    Clase para definir rutas relacionadas con ejemplos.
    """
    def __init__(self):
        self.router = APIRouter()
        self.controller = ExampleController()
        self._register_routes()

    def _register_routes(self):
        @self.router.get("/example")
        def example_endpoint():
            return self.controller.fetch_data()

        @self.router.post("/example")
        def create_example(example: ExampleDTO):
            """
            Endpoint que recibe datos para crear un ejemplo.
            """
            return self.controller.create_example(example.dict())

# Instancia de la clase router para su uso en main.py
example_router = ExampleRouter().router