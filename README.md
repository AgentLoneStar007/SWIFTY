# S.W.I.F.T.Y
### *Stream Web-based Interaction Frontend for Twitch and YouTube*

---
The website for LoneStar Gaming's streams, which allows for store redemptions,
soundboard usage, and more (in the future)!

This website is made in Python and uses a Flask webserver under the hood. If you
want to fork this repository and make something similar, feel free to! This project
is licensed under the MIT open-source license, so go crazy.

## Getting Started:

--- 
Prerequisites:
- Python
- A brain

### 1: Install requirements
#### 1.1: Install requirements using system-wide Python install
This can be done via the pip command, if you're using the Pip package manager. If you're
not, then you  probably skipped this part anyway.<br />
Make sure you're in the directory of the cloned Git repository, then run either of
the following commands, using whichever works.

`pip install -r requirements.txt`

OR

`python -m pip install -r requirements.txt`

Which should install all needed project requirements.
#### 1.2: Install requirements in a virtual environment
If you want to instead create a virtual environment in which to run Python, you can do
so by running the following commands:

`python -m venv .venv/`

Which would install the virtual environment in a directory named ".venv/"
Then activate the virtual environment using the command for your operating system.

Linux:<br />
`source .venv/bin/activate`

Windows:<br />
`.venv\Scripts\activate`

Finally, run the command to install the requirements.

`pip install -r requirements.txt`

### 2: Start the development server
To start the server, simply run the `run.py` Python script.

`python run.py`

The default port is 8080, which *shouldn't* conflict with any other ports. But if you
get an error when trying to start the server, change the port to something else.

### 3: Run in production
TODO: Write this part.
