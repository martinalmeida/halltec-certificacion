from fastapi import APIRouter, Header
from app.controllers.auth_controller import AuthController
from app.controllers.range_controller import RangeController

class Router:

    def __init__(self):
        self.router = APIRouter()
        self.auth_controller = AuthController()
        self.range_controller = RangeController()
        self._register_routes()
    
    def _register_routes(self):

        @self.router.get("/get-token")
        async def get_token():
            return await self.auth_controller.send_auth_token()

        @self.router.get("/get-range")
        async def get_range(authorization: str = Header(...)):
            return await self.range_controller.send_get_range(authorization)

router = Router().router