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

from app.logs import logManager
from pprint import pprint

class PageBuilder(object):
    """ The PageBuilder ...
    """

    def __init__(self, ):
        # preparation to instanciate
        pass

    def init_builder(self,  app, db, userManager, workspaceManager):
        self.app = app
        self.db = db
        self.workspaceManager = workspaceManager
        self.userManager = userManager    
