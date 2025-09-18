# Imports
from flask import Flask
from .routes import createRoutes
import tomllib


def createApp(app_name: str) -> Flask:
    """
    Creates and returns a full Flask app, with the main
    route and context globals all registered.

    :param app_name: The app's name. Get this from the config.

    :returns: ``Flask`` - A Flask app.

    :raises None:
    """

    # Fetch the program configuration
    config: dict = tomllib.load(open("config.toml", "rb"))

    # Create the API app
    app: Flask = Flask(
        app_name,
        static_url_path="",
        static_folder="app/web/static",
        template_folder="app/web/templates"
    )

    # Register blueprints
    app.register_blueprint(createRoutes())

    # Create global values that's passed to every page
    @app.context_processor
    def inject_globals():
        return {
            "app_name": config.get("app_name", "{channel_name}"),
            "icon_url": config.get("icon_url", "/images/favicon.ico"),
            "channel_name": config.get("channel_name", "{channel_name}"),
            "enable_twitch": config.get("enable_twitch", True),
            "enable_youtube": config.get("enable_youtube", True),
            "enable_store": config.get("enable_store", True),
            "enable_soundboard": config.get("enable_soundboard", True),
            "enable_tips_page": config.get("enable_tips_page", True),
            "enable_about_me_page": config.get("enable_about_me_page", True),
            "enable_links_page": config.get("enable_links_page", True)
        }

    return app



