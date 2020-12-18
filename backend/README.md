# roseguarden backend

## Install required packages

`pip3 install -r requirements.txt` to install the dependencies.

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
