from fastapi import APIRouter
from src.http_client import CMCClient
from src.config import settings

cmc_client = CMCClient(
    "https://pro-api.coinmarketcap.com",
    settings.CMC_API_KEY

)

crypto_router = APIRouter(
    prefix="/cryptocurrency"
)

@crypto_router.get("")
async def get_crypto_currencies():
    return await cmc_client.get_listing()

@crypto_router.get("/{symbol}")
async def get_crypto_by_symbol(symbol_crypto: str):
    return await cmc_client.get_crypto_by_symb(symbol_crypto)

