from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Webhook.webhook import webhook_router

app = FastAPI ()

app.include_router (router=webhook_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # 1
    allow_credentials=True,   # 2
    allow_methods=["*"],      # 3
    allow_headers=["*"],      # 4
)