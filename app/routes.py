# Imports
from flask import Blueprint, render_template
import tomllib


def createRoutes() -> Blueprint:
    """
    Creates and returns the main blueprint for routes,
    automatically handling which routes to register based
    on the configuration.

    :returns: ``Blueprint`` - A Flask blueprint.

    :raises None:
    """

    # Fetch the program configuration
    config: dict = tomllib.load(open("config.toml", "rb"))

    # Create the main (maybe temporarily named) route
    main: Blueprint = Blueprint("main", __name__)

    # Set the response for the root prefix
    @main.route("/")
    def index() -> str:
        return render_template("index.html")

    # Only register the store route if it's enabled
    if config.get("enable_store", True):
        @main.route("/store")
        def storePage() -> str:
            return render_template("store.html")

    # Only register the soundboard route if it's enabled
    if config.get("enable_soundboard", True):
        @main.route("/soundboard")
        def soundboardPage() -> str:
            return render_template("soundboard.html")

    # Only register the tips route if it's enabled
    if config.get("enable_tips_page", True):
        @main.route("/tips")
        def tipsPage() -> str:
            return render_template("tips.html")

    # Only register the about me route if it's enabled
    if config.get("enable_about_me_page", True):
        @main.route("/about-me")
        def aboutMePage() -> str:
            return render_template("about_me.html")

    # Only register the links route if it's enabled
    if config.get("enable_links_page", True):
        @main.route("/links")
        def linksPage() -> str:
            return render_template("links.html")

    return main
