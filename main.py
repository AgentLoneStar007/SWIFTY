## S.W.I.F.T.Y
## A website and websocket server that allows viewers of streams across YouTube
## and Twitch to interact with streams via Streamer.bot.
## Created by AgentLoneStar007, licensed under the MIT license.

# Imports
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import tomllib

# Fetch the program configuration
config: dict = tomllib.load(open("config.toml", "rb"))

# Create the API app
app: FastAPI = FastAPI(
    title=config.get("app_name", "S.W.I.F.T.Y"),
    version=config.get("version", "{version}"),
)

# Include templates
templates: Jinja2Templates = Jinja2Templates(directory="templates")

# Include routers
# app.include_router(coming_soon, prefix="/coming-soon")

# Set the response for the root prefix
@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "app_name": config.get("app_name", "S.W.I.F.T.Y"),
            "channel_name": config.get("channel_name", "{channel_name}")
        }
    )
