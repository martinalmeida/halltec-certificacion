from app.services.municipality_service import MunicipalityService
from fastapi import Header, HTTPException
from dotenv import load_dotenv
import os

class MunicipalityController:

    def __init__(self):
        self.municipality_service = MunicipalityService()
        load_dotenv()

    async def send_get_municipality(self, authorization: str = Header(...)):
        try:
            if not authorization.startswith("Bearer "):
                raise HTTPException(status_code=400, detail="Invalid token format")
                
            token = authorization.split("Bearer ")[1]
            url = os.getenv("APP_URL") + "v1/municipalities"
            response = await self.municipality_service.municipalities(url, token)
            return {
                "status": "success",
                "data": response
            }
        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }