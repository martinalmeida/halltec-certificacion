from fastapi import APIRouter
from app.controllers.auth_controller import AuthController

class Router:

    def __init__(self):
        self.router = APIRouter()
        self.controller = AuthController()
        self._register_routes()
    
    def _register_routes(self):

        @self.router.get("/get-token")
        async def get_token():
            return await self.controller.send_auth_token()

router = Router().router