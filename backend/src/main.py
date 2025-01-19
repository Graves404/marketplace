from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import crypto_currencies, user_router, auth_router, items_router

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router.user_router)
app.include_router(auth_router.auth_router)
app.include_router(items_router.item_router)
app.include_router(crypto_currencies.crypto_router)
