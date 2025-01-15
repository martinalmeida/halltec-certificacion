import httpx

class InvoiceService:

    async def create_invoice(self, url: str, payload: dict, token: str):
        async with httpx.AsyncClient() as client:
            headers = {"Authorization": f"Bearer {token}"}
            try:
                response = await client.post(url, headers=headers, json=payload)
                response.raise_for_status()
                return response.json()
            except httpx.HTTPStatusError as e:
                raise Exception(e.response.json())