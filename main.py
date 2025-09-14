from fastapi import FastAPI
from Webhook.webhook import webhook_router

app = FastAPI ()

app.include_router (router=webhook_router)