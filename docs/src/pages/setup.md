---
title: Installation
---

# Setup Roseguarden-Server

Es gibt mehrere Wege den Roseguarden-Server zum laufen zu bekommen:

1. By using Docker for Development (recommended)

- run `docker-compose up -d`
- change frontend/nuxt.config.js change proxy-targets to: target: http://backend:5000 for /api/v1 and /api/v1/log
- frontend is listening on localhost:3000
- backend is listening on localhost:8002 (e.g. for direct calls via insomnia)

:boom: **Note:** the first command is caching an `npm install` into a named docker volume, which is then used in docker-compose. If you change anything in package.json rerun the first command to update dependencies.

2. By using the release packages

- Download and unzip the latest release `roseguarden-X.Y.Z` [here](https://gitlab.com/roseguarden/roseguarden/-/releases)
- Go to the folder and run the following commands in a terminal
  - Install the requirements with `pip3 -r requirements.txt`
  - Create a `config.ini` with your settings (see `config.template`)
  - Run 'flask run'

3. By cloning or forking the roseguarden repository

- Clone or fork https://gitlab.com/roseguarden/roseguarden
- Have a look in the `backend` and `frontend` folder for details to setup your development enviroment
- run `backend` and `frontend` from your development environment (e.g. we use vs code)
  - start the backend with `flask run` out of the `backend` folder (see more datailed instructions below)
  - start the frontend with `npm run dev` out of the `frontend` folder

* alternativly you can use the `script/pack.py`-script to build your own package and host it with an HTTP-server

  3.1. Run Backend after fresh clone:

- `cd backend`
- `python3 -m venv .venv`
- `. venv/bin/activate`
- (venv) `pip install Flask`
- (venv) `pip install -r requirements.txt`
- (venv) `run flask`
