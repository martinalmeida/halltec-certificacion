from fastapi import APIRouter, Header
from app.controllers.auth_controller import AuthController
from app.controllers.range_controller import RangeController
from app.controllers.municipality_controller import MunicipalityController
from app.controllers.tribute_controller import TributeController
from app.controllers.unit_measurement_controller import UnitMeasurementController
from app.controllers.invoice_controller import InvoiceController
from app.schemas.invoice_schema import InvoiceSchema

class Router:

    def __init__(self):
        self.router = APIRouter()
        self.auth_controller = AuthController()
        self.range_controller = RangeController()
        self.municipality_controller = MunicipalityController()
        self.tribute_controller = TributeController()
        self.unit_measurement_controller = UnitMeasurementController()
        self.invoice_controller = InvoiceController()
        self._register_routes()
    
    def _register_routes(self):

        @self.router.get("/get-token")
        async def get_token():
            return await self.auth_controller.send_auth_token()

        @self.router.get("/get-range")
        async def get_range(authorization: str = Header(...)):
            return await self.range_controller.send_get_range(authorization)
        
        @self.router.get("/get-municipality")
        async def get_municipality(authorization: str = Header(...)):
            return await self.municipality_controller.send_get_municipality(authorization)

        @self.router.get("/get-tribute")
        async def get_tribute(authorization: str = Header(...)):
            return await self.tribute_controller.send_get_tribute(authorization)
        
        @self.router.get("/get-measures")
        async def get_measures(authorization: str = Header(...)):
            return await self.unit_measurement_controller.send_get_measures(authorization)
        
        @self.router.post("/create-invoice")
        async def create_invoice(invoice: InvoiceSchema, authorization: str = Header(...)):
            return await self.invoice_controller.send_create_invoice(invoice.model_dump(), authorization)

router = Router().router