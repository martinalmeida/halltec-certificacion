from app.services.auth_service import AuthService
from dotenv import load_dotenv
import os

class AuthController:

    def __init__(self):
        self.auth_service = AuthService()
        load_dotenv()

    async def send_auth_token(self):
        try:
            auth_url = os.getenv("APP_URL") + "oauth/token"
            payload = {
                "grant_type": "password",
                "client_id": os.getenv("CLIENT_ID"),
                "client_secret": os.getenv("CLIENT_SECRET"),
                "username": os.getenv("EMAIL"),
                "password": os.getenv("PASSWORD")
            }
            response = await self.auth_service.oauth_token(auth_url, payload)
            return {
                "status": "success",
                "data": response
            }
        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }