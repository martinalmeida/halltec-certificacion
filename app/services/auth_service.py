import httpx

class AuthService:

    async def oauth_token(self, url: str, payload: dict):
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(url, json=payload)
                response.raise_for_status()
                return response.json()
            except httpx.HTTPStatusError as e:
                raise Exception(e.response.json())