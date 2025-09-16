from dotenv import load_dotenv
from httpx import AsyncClient
import os


client = AsyncClient ()
load_dotenv ()

verifyToken = os.getenv ("VERIFY_TOKEN")
accessToken = os.getenv ("ACCESS_TOKEN")

async def initClient ():
    global client
    client = AsyncClient ()
    return None
    

async def sendMessage (id:str, phoneNO:str, message:str) -> str:
    url = f"https://graph.facebook.com/v23.0/{id}/messages"
    header = {
        'content-type': 'application/json',
        'Authorization': f'Bearer {accessToken}'
    }

    payload = {
        'messaging_product': 'whatsapp',
        'to': phoneNO,
        'type': 'text',
        'text': {
            'body': message
            }
        }

    response = await client.post (url=url, headers=header, json=payload)
    return response.text