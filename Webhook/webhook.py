from fastapi import APIRouter, Request, Query
from fastapi.responses import PlainTextResponse
import json
from datetime import datetime, timezone
from Webhook.utils import verifyToken

webhook_router = APIRouter (prefix="/webhook", tags=['Webhook'])

@webhook_router.get ("/verify")
async def verify_webhook (
    hub_mode:str = Query (None, alias="hub.mode"),
    hub_challenge:str = Query (None, alias="hub.challenge"),
    hub_verify_token:str = Query (None, alias="hub.verify_token")
):
    print (f"{hub_mode}  {hub_challenge}  {hub_verify_token}")
    print (verifyToken)
    if hub_mode == 'subscribe' and hub_verify_token == verifyToken:
        print ('Webhook Verified')
        return PlainTextResponse (content=hub_challenge, status_code=200)
    else:
        return PlainTextResponse (content='Forbidden', status_code=403)
    
@webhook_router.post ("/message")
async def receive_webhook (request: Request):
    body = await request.json ()
    timestamp = datetime.now(timezone.utc).strftime ("%Y-%m-%d %H:%M:%S")

    print(f"\n\n📩 Webhook received at {timestamp}\n")
    print(json.dumps(body, indent=2))

    return PlainTextResponse (content="EVENT_RECEIVED", status_code=200)