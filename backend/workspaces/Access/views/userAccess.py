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
__contact__ = "roseguarden@fabba.space"
__credits__ = []
__license__ = "GPLv3"

from core.workspaces import DataView, Workspace
from core.users.models import User
from core import db
import arrow

from workspaces.Access.permissions import ViewAccessGroups
from workspaces.Access.models import SpaceAccessGroup, SpaceAccessProperties
""" A view contaning the list of accessGroups
"""


class AccessGroupsList(DataView):

    uri = 'accessUserList'
    requireLogin = True

    def defineProperties(self):
        self.addMailProperty(name='email', label='User email', isKey=True)
        self.addStringProperty(name='name', label='User name')
        self.addIntegerProperty(name="access_group", label="Access group")
        self.addIntegerProperty(name="access_type", label="Access type")
        self.addIntegerProperty(name='access_budget', label='Budget')
        self.addDateProperty(name='access_start_date', label='Valid from')
        self.addDateProperty(name='access_end_date', label='Valid to')
        self.addDateProperty(name='access_last_update', label='Last updated', readOnly=True)

    def getViewHandler(self, user: User, workspace: Workspace, query=None):
        print("getDataViewHandler for AccessUserList")
        userlist = []
        all_user = User.query.filter_by(account_locked=False).all()
        for u in all_user:
            # get new empty entry
            entry = self.createEntry()
            # fill entry
            entry.email = u.email
            entry.name = "{0} {1}".format(u.firstname, u.lastname)
            if u.access is not None:
                entry.access_budget = u.access.access_budget
                entry.access_start_date = u.access.access_start_date.format('YYYY-MM-DD')
                entry.access_end_date = u.access.access_expire_date.format('YYYY-MM-DD')
                entry.access_last_update = u.access.access_last_update_date.format('YYYY-MM-DD')
            else:
                entry.access_start_date = "-"
                entry.access_end_date = "-"
                entry.access_last_update = "-"

            if u.accessgroup is not None:
                entry.access_type = u.accessgroup.access_type
                entry.access_group = u.accessgroup.id
            else:
                entry.access_group = -1
                entry.access_type = "-"

            userlist.append(entry.extract())
        return userlist

    def __repr__(self):
        return '<{} with {} properties>'.format(self.name, len(self.properties))

    # Handler for a request to create a new view entry
    def createViewEntryHandler(self, user, workspace, entry):
        raise Exception("User creation not allowed in userAccess view")

    # Handler for a request to update a single view entry
    def updateViewEntryHandler(self, user, workspace, key, entry):
        print("Handle updateViewEntryHandler request for " + self.uri)
        u = User.query.filter_by(email=key).first()
        u.access.access_last_update_date = arrow.utcnow()
        if hasattr(entry, 'access_budget'):
            u.access.access_budget = entry.access_budget
        if hasattr(entry, 'access_start_date'):
            u.access.access_start_date = arrow.get(entry.access_start_date, 'YYYY-MM-DD')
        if hasattr(entry, 'access_group'):
            g = SpaceAccessGroup.query.filter_by(id=entry['access_group']).first()
            u.accessgroup = g
        if hasattr(entry, 'access_expire_date'):
            u.access.access_end_date = arrow.get(entry.access_expire_date, 'YYYY-MM-DD')
        self.emitSyncUpdate(key)

    # Handler for a request to update a single view entry
    def removeViewEntryHandler(self, user, workspace, key):
        raise Exception("User removal not allowed in userAccess view")
