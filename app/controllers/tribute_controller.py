from app.services.tribute_service import TributeService
from fastapi import Header, HTTPException
from dotenv import load_dotenv
import os

class TributeController:

    def __init__(self):
        self.tribute_service = TributeService()
        load_dotenv()

    async def send_get_tribute(self, authorization: str = Header(...)):
        try:
            if not authorization.startswith("Bearer "):
                raise HTTPException(status_code=400, detail="Invalid token format")
                
            token = authorization.split("Bearer ")[1]
            url = os.getenv("APP_URL") + "v1/tributes/products"
            response = await self.tribute_service.tributes(url, token)
            return {
                "status": "success",
                "data": response
            }
        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }