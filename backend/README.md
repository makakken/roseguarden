# roseguarden backend

## Getting started

Before we start, we have to prepare ourself.
### Create virtual environment

Before we install the dependencies, we create a virtual environment. This process depends on your OS.

#### Linux
Open a terminal and unstall `python3-venv` with
```
sudo apt-get install python3-venv
```
Go to the backend directory
```
cd /path/to/roseguard/backend/directory
```
Now we create a virtual environment with:
```
python3 -m venv .venv
```
The flag `-m` tells python to run the *venv* library module as a script. The name of our new virtual environment is *.venv*.
To activate the virtual environment run
```
source .venv/bin/activate
```
You should see now `(.venv)` at the very beginning of your terminal line.

#### Windows
⚠️ At the moment (20.12.2020) it is not possible to run the roseguarden backend with native python directly on Windows, because some python packages like [bcrypt](https://pypi.org/project/bcrypt/) can not be installed on Windows.

But you can install it in a **WSL2 distribution** or you use **anaconda** to realise a virtual environment.

###  Install required packages
To install all dependencies run
```
pip3 install -r requirements.txt
```

Only python3 packages are needed.

### Configure

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
                "FLASK_APP": "app.py",
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

## Developer setup

### 🐧 Linux/macOS

Open a terminal and create a new virtual environment in your home directory with the name `.toxbase` with the following commands

```bash
# Change to your user directory
$ cd ~
# Create a virtual environment called .toxbase
$ python -m venv .toxbase
```

Now we activate the virtual environment, update pip and install tox:

**Linux/maxOS:**
``` bash
# Linux/macOS
$ source .toxbase/bin/activate
```
**Windows:**

```
.\.toxbase\Scripts\Activate.ps1
``` 

Update pip and install tox

``` bash
# the virtual environment is active
# if you see the environment name at the beginning of the line
(.toxbase) $ python -m pip install --upgrade pip
(.toxbase) $ pip install tox
(.toxbase) $ tox --version
```



Setting the PATH variable

```bash
cd
# open the config file .bashrc
nano .bashrc
# Go to the buttom of the file and insert
# make tox accessable in each session from everywhere
PATH = "${HOME}/bin:${PATH}"
export PATH
# save and close the file with CTRL+O and CTRL+X
# create a `bin` directory 
mkdir bin
# set link to ~/bin/tox
ln -s ~/.toxbase/bin/tox ~/bin/tox
```

```bash
# open a new terminal session and test tox
tox --version
# this command should give you something similiar like
3.20.1 imported from /home/YourUserName/.toxbase/lib/python3.8/site-packages/tox/__init__.py
```

⚠ You have to replace `YourUserName` with your actual *username* in the
path!

To make all these changes work you have to log out and in again.

To get the same working environment you can just run
```bash
tox -e dev
```
This will create a virtual environment with all our development tools.

Later you can run just 
```bash
tox
```
to run our tests and linter.