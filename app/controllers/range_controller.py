from app.services.range_service import RangeService
from fastapi import Header, HTTPException
from dotenv import load_dotenv
import os

class RangeController:

    def __init__(self):
        self.range_service = RangeService()
        load_dotenv()

    async def send_get_range(self, authorization: str = Header(...)):
        try:
            if not authorization.startswith("Bearer "):
                raise HTTPException(status_code=400, detail="Invalid token format")
                
            token = authorization.split("Bearer ")[1]
            url = os.getenv("APP_URL") + "v1/numbering-ranges"
            response = await self.range_service.ranges(url, token)
            return {
                "status": "success",
                "data": response
            }
        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }