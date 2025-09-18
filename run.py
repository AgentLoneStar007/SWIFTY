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

# TODO(s)
#  - Make a simple method of creating new soundboard items,
#    so simple that even streamers can figure it out.
#  - Figure out dashboard layout
#  - Figure out OAuth with Twitch and YouTube
#    Two methods of doing this are to do it the
#    right way (by setting up auth with both
#    platforms), or figure out a system of either
#    session linking via running a command in chat,
#    or by creating an account stored on this webserver
#    and then linking said account to your Twitch and YT
#    accounts via the previously mentioned command. But
#    creating local accounts would probably be an issue
#    because people think it's funny to create 1e2.34
#    accounts within 43ms.
#  - Figure out the store. I really don't like the idea
#    of handling credit card info in this app...
#  - Translations?
#  And I think that's it!


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
