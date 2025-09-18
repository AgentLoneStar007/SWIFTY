## S.W.I.F.T.Y
## A website and websocket server that allows viewers of streams across YouTube
## and Twitch to interact with streams via Streamer.bot.
## Created by AgentLoneStar007, licensed under the MIT license.

# Imports
from app import createApp
from flask import Flask
import tomllib
import sys
import traceback


# Main program loop
def main() -> None:
    # Fetch the program configuration
    config: dict = tomllib.load(open("config.toml", "rb"))

    # Create the app
    app: Flask = createApp(config.get("app_name", "S.W.I.F.T.Y"))

    # And start the server
    app.run(
        port=int(config.get("port", 8080)),
        debug=bool(config.get("run_in_debug_mode", True))
    )


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Shutting down!")
        sys.exit(0)

    except Exception as error:
        print(f"Error occurred! {error}")
        traceback.print_exc()
        sys.exit(1)
