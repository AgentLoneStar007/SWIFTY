# Imports
from flask import Flask
from .routes import main


def create_app(app_name: str) -> Flask:
    # Create the API app
    app: Flask = Flask(
        app_name,
        static_url_path="",
        static_folder="app/web/static",
        template_folder="app/web/templates"
    )

    # Register blueprints
    app.register_blueprint(main)

    return app



