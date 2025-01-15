import httpx

class TributeService:

    async def tributes(self, url: str, token: str):
        async with httpx.AsyncClient() as client:
            headers = {"Authorization": f"Bearer {token}"}
            try:
                response = await client.get(url, headers=headers)
                response.raise_for_status()
                return response.json()
            except httpx.HTTPStatusError as e:
                raise Exception(e.response.json())