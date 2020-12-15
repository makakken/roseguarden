""" 
The roseguarden project 

Copyright (C) 2018-2020  Marcus Drobisch,

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.
"""

__authors__ = ["Marcus Drobisch"]
__contact__ =  "roseguarden@fabba.space"
__credits__ = []
__license__ = "GPLv3"

import logging
import datetime

from flask import Flask, Blueprint, request, current_app, jsonify, redirect, url_for, send_from_directory
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS, cross_origin

version = "0.2.1"


from config import configure_app, load_config
from app.logs import logManager
from app.workspaces import workspaceManager
from app.nodes import nodeManager
from app.users import userManager
from app.messages import messageManager
from app.jobs import jobManager
from app.actions import actionManager
from app.files import fileManager
from app.menus import menuBuilder

jwt = JWTManager()
db = SQLAlchemy()
bcrypt = Bcrypt()
migrate = Migrate()

def create_app(minimal = False):
    config = load_config("config.ini")
    app = Flask(__name__, static_folder = "./dist")
    # configure the app
    configure_app(app, config)

    if __name__ != '__main__':
        gunicorn_logger = logging.getLogger('gunicorn.error')
        app.logger.handlers = gunicorn_logger.handlers
        app.logger.setLevel(gunicorn_logger.level)

    #logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')


    if not minimal:
        cors = CORS(app)
        logManager.init_app(app)
        logManager.info("Started roseguarden: " + version)
        jwt.init_app(app)
        workspaceManager.discoverModels()
        bcrypt.init_app(app)

    from app import app_bp
    app.register_blueprint(app_bp)

    from app.actions import actions_bp, models
    app.register_blueprint(actions_bp)

    from app.users import auth_bp, models
    app.register_blueprint(auth_bp)

    from app.logs import logs_bp
    app.register_blueprint(logs_bp)

    from app.jobs import jobs_bp
    app.register_blueprint(jobs_bp)

    from app.messages import messages_bp
    app.register_blueprint(messages_bp)

    from app.files import files_bp
    app.register_blueprint(files_bp)

    from app.nodes import nodes_bp
    app.register_blueprint(nodes_bp)

    # import workspace blueprint and models
    from app.workspaces import workspaces_bp
    from app.workspaces import models

    app.register_blueprint(workspaces_bp)

    from api import api_bp
    app.register_blueprint(api_bp)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    if not minimal:
        migrate.init_app(app, db)
        jobManager.init_manager(app,db, config)
        workspaceManager.init_app(app, db)
        userManager.init_manager(app, db, workspaceManager, config)
        nodeManager.init_manager(app,db, workspaceManager)
        messageManager.init_manager(app,db, workspaceManager, config)
        menuBuilder.init_builder(app, db, userManager, workspaceManager)    
        actionManager.init_manager(app, db, userManager, menuBuilder, workspaceManager, nodeManager, config)
        fileManager.init_manager(app,db, workspaceManager, config)


    return app


# declare app routes
app_bp = Blueprint('app', __name__, static_folder = "../dist")
from app import routes