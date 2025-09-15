# Imports
from flask import Blueprint, render_template
import tomllib

# Fetch the program configuration
config: dict = tomllib.load(open("config.toml", "rb"))

# Create the main (maybe temporarily named) route
main: Blueprint = Blueprint("main", __name__)

# Set the response for the root prefix
@main.route("/")
def index() -> str:
    return render_template(
        "index.html",
        app_name=config.get("app_name", "{channel_name}"),
        channel_name=config.get("channel_name", "{channel_name}")
    )
