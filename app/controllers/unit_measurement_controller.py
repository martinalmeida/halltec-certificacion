from app.services.unit_measurement_service import UnitMeasurementService
from fastapi import Header, HTTPException
from dotenv import load_dotenv
import os

class UnitMeasurementController:

    def __init__(self):
        self.unit_measurement_service = UnitMeasurementService()
        load_dotenv()

    async def send_get_measures(self, authorization: str = Header(...)):
        try:
            if not authorization.startswith("Bearer "):
                raise HTTPException(status_code=400, detail="Invalid token format")
                
            token = authorization.split("Bearer ")[1]
            url = os.getenv("APP_URL") + "v1/measurement-units"
            response = await self.unit_measurement_service.measures(url, token)
            return {
                "status": "success",
                "data": response
            }
        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }