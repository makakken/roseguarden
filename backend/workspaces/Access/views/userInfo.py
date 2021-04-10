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

from core.workspaces.workspace import Workspace
from core.workspaces.dataView import DataView
from core.users.models import User

from workspaces.Access.types import get_access_info_string
from workspaces.Access.helpers import get_user_accessable_weekdays_string, get_accessable_spaces_for_user_string
""" A View contaning the user info


Deine Zugangsgruppe: 10er Karten  (info = Alle User mit einer Zehnerkarte) 
Gültig bis: 30.1.2022
Zugangstyp: Budget an Tagen
Verbleibendes Budget: 5 Tage
Zugang zu folgenden Räumen: Konglomerat, RON
Zugang an folgenden Tagen: Mo, Di, Mi, Do, Fr, Sa, So.
Zugang in folgendem Zeitraum: 00:00 bis 23:59
Letztes Update: 25.03.2020

"""


class AccessUserInfo(DataView):

    uri = 'userInfo'
    requireLogin = True

    def defineProperties(self):
        self.addMailProperty(name='email', isKey=True)
        self.addStringProperty(name='access_group')
        self.addStringProperty(name='access_group_info')
        self.addStringProperty(name='access_type')
        self.addStringProperty(name='access_type_info')
        self.addIntegerProperty(name='access_budget')
        self.addDateProperty(name='access_valid_start_date')
        self.addDateProperty(name='access_valid_end_date')
        self.addTimeProperty(name='access_valid_start_time')
        self.addTimeProperty(name='access_valid_end_time')
        self.addStringProperty(name='access_to_spaces')
        self.addStringProperty(name='access_on_days')
        self.addDateProperty(name='access_updated_on_date')

    def getViewHandler(self, user: User, workspace: Workspace, query=None):
        # get new empty entry
        entry = self.createEntry()
        # fill entry
        entry.email = user.email
        entry.access_updated_on_date = user.access.access_last_update_date.format('YYYY-MM-DD')
        if user.accessgroup is not None:
            entry.access_group = user.accessgroup.name
            entry.access_group_info = user.accessgroup.note
            entry.access_type = user.accessgroup.access_type.value
            entry.access_type_info = get_access_info_string(user.accessgroup, user.access)
            entry.access_valid_start_date = user.access.access_start_date.format('YYYY-MM-DD')
            entry.access_on_days = get_user_accessable_weekdays_string(user.accessgroup)
            if user.access.access_expires is False:
                entry.access_valid_end_date = "Never"
            else:
                entry.access_valid_end_date = user.access.access_expire_date.format('YYYY-MM-DD')
            entry.access_to_spaces = get_accessable_spaces_for_user_string(user.accessgroup)
            entry.access_valid_start_time = user.accessgroup.daily_access_start_time.format('HH:mm')
            entry.access_valid_end_time = user.accessgroup.daily_access_end_time.format('HH:mm')
        else:
            entry.access_group = "No group"
            entry.access_group_info = "You are not in a access group at the moment"
            entry.access_type_info = "You don't have any access at the moment"
            entry.access_to_spaces = "None"
            entry.access_on_days = "None"
            entry.access_valid_start_time = "-"
            entry.access_valid_end_time = "-"
            entry.access_valid_start_date = "-"
            entry.access_valid_end_date = "-"
        # add single entry
        return entry.extract()

    def __repr__(self):
        return '<{} with {} properties>'.format(self.name, len(self.properties))

    # Handler for a request to create a new view entry
    def createViewEntryHandler(self, user, workspace, entry):
        print("Handle createViewEntry request for " + self.uri)

    # Handler for a request to update a single view entry
    def updateViewEntryHandler(self, user, workspace, key, entry):
        print("Handle updateViewEntryHandler request for " + self.uri)
