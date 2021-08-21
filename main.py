import asyncio
import json

import aiohttp
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
duck_query = 'http://api.duckduckgo.com/?q={}&format=json'


async def extract_content(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


@app.get("/{param}")
async def read_root(param: str):
    j = json.loads(await extract_content(duck_query.format(param)))
    s = await extract_content(j['AbstractURL'])
    return HTMLResponse(content=s, status_code=200)


@app.get("/")
async def empty_request():
    return {"result": "Please provide a search query."}
