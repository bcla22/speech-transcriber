from sanic import Sanic
from sanic.response import json, HTTPResponse
from sanic.request import Request

app = Sanic("speech-transcriber")

@app.middleware("response")
async def cors_headers(request, response):
    response.headers["Access-Control-Allow-Origin"] = "*"


@app.get("/")
async def root(request: Request) -> HTTPResponse:
    return json({"status": "ok"})


@app.post("/transcribe")
async def transcribe(request: Request) -> HTTPResponse:
    files = request.files
    
    if len(files) != 1:
        return json({"error": "missing upload files"}, status=400)
    

    return json(True)
