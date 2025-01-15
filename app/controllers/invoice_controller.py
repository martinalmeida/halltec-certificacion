from app.services.invoice_service import InvoiceService
from fastapi import Header, HTTPException
from dotenv import load_dotenv
import os

class InvoiceController:

    def __init__(self):
        self.invoice_service = InvoiceService()
        load_dotenv()

    async def send_create_invoice(self, payload: dict, authorization: str = Header(...)):
        try:
            if not authorization.startswith("Bearer "):
                raise HTTPException(status_code=400, detail="Invalid token format")
                
            token = authorization.split("Bearer ")[1]
            url = os.getenv("APP_URL") + "v1/bills/validate"
            response = await self.invoice_service.create_invoice(url, payload, token)
            return {
                "status": "success",
                "data": response
            }
        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }