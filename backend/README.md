# roseguarden backend

## Getting started

Before we start, we have to prepare ourself.

⚠️ At the moment (20.12.2020) it is not possible to run the roseguarden backend on Windows, because some python packages like [bcrypt](https://pypi.org/project/bcrypt/) can not be installed on Windows.
But you can install it in a WSL2 distribution.

### Create virtual environment
Before we install the dependencies, we create a virtual environment. For this we open a terminal and go to the backend directory.

There we create a virtual environment with:
```
python3 -m venv .venv
```
The flag `-m` tells python to run the *venv* library module as a script. The name of our new virtual environment is *.venv*.
To activate the virtual environment run
```
source .venv/bin/activate
```
You should see now `(.venv)` at the very beginning of your terminal line.

###  Install required packages
To install all dependencies run
```
pip3 install -r requirements.txt
```

Only python3 packages are needed.

## Configure

create a `config.ini` in the the backend folder.

Use `config.template` as a template for available configs.


## Run the app

### Option 1 : Run with python3

`python3 app.py` in the backend folder

### Option 2 : Run with flask

`flask run` in the backend folder

### Option 3 : Run in VS Code

Add a entry in the `launch.json` (e.g. from the run menu)

```
    "configurations": [
        {
            "name": "Python: Flask",
            "type": "python",
            "request": "launch",
            "module": "flask",
            "env": {
                "FLASK_APP": "server.py",
                "FLASK_ENV": "development",
                "FLASK_DEBUG": "0"
            },
            "args": [
                "run",
                "--no-debugger",
                "--no-reload"
            ],
            "jinja": true
        }
    ]
```

## Debug and develop roseguarden in VS Code

https://code.visualstudio.com/docs/python/tutorial-flask
