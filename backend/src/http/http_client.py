from aiohttp import ClientSession

class HTTPClient:
    def __init__(self, base_url_: str, api_key: str):
        self._session = ClientSession(
            base_url=base_url_,
            headers={
                'X-CMC_PRO_API_KEY': api_key,
            }
        )

class CMCClient(HTTPClient):
    async def get_listing(self):
        async with self._session.get("/v1/cryptocurrency/listings/latest") as resp:
            res = await resp.json()
            return res["data"]

    async def get_crypto_by_symb(self, symbol_: str):
        async with self._session.get(
            "/v2/cryptocurrency/quotes/latest",
            params={"symbol": symbol_}
        ) as resp:
            res = await resp.json()
            return res["data"][str(symbol_)]
