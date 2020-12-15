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

from app.workspaces import DataView, Workspace
from app.users.models import User
from app import db
import arrow

from workspaces.Access.permissions import ViewAccessGroups
from workspaces.Access.models import SpaceAccessGroup, SpaceAccessSpace

""" A view contaning the list of accessGroups
"""
class AccessGroupsList(DataView):

    uri = 'accessGroupsList'
    requireLogin = True

    def defineProperties(self):        
        self.addIntegerProperty(name='id', label='ID', isKey=True)
        self.addStringProperty(name='name', label='Name')
        self.addStringProperty(name='note', label='Note')
        self.addSelectProperty(name='type', label='Access type', selectables=['No access', 
                                                                            'Unlimited', 
                                                                            'Fixed day budget',
                                                                            'Auto-charged budget (monthly)',
                                                                            'Auto-charged budget (weekly)'])
        self.addBooleanProperty(name='budget_needed', label='Need budget')
        self.addBooleanProperty(name='expires_as_default', label='Expires (as default)')
        self.addIntegerProperty(name='expires_after_days', label='Expires (days default)')
        self.addMultiSelectProperty(name='spaces', label='Space keys', selectables=[])
        self.addIntegerProperty(name='days_mask', label='Accessable days')
        self.addTimeProperty(name='daily_start_time', label='Daily start time')
        self.addTimeProperty(name='daily_end_time', label='Daily end time')


    def getViewHandler(self, user: User, workspace: Workspace, query=None):
        print("getDataViewHandler for AccessGroupsList")
        entrylist = []
        all_groups = SpaceAccessGroup.query.all()
        for g in all_groups:

            # get new empty entry
            entry = self.createEntry()

            # fill entry
            entry.id = g.id
            entry.name = g.name
            entry.note = g.note
            entry.type = g.access_type
            entry.daily_start_time = g.daily_access_start_time.format('HH:mm') 
            entry.daily_end_time = g.daily_access_end_time.format('HH:mm') 
            entry.spaces = []
            for si in g.spaces:
                entry.spaces.append(si.id)

            entry.days_mask = g.day_access_mask
            entry.expires_as_default = g.access_expires_as_default
            entry.expires_after_days = g.access_expires_default_days
            entry.budget_needed = g.access_need_budget

            entrylist.append(entry.extract())
        return entrylist

    def __repr__(self):
        return '<{} with {} properties>'.format(self.name, len(self.properties))

    # Handler for a request to create a new view entry 
    def createViewEntryHandler(self, user, workspace, entry):
        ag = SpaceAccessGroup()
        if hasattr(entry, 'name'):
            ag.name = entry.name
        else:
            ag.name = "New group"
        ag.note = "Add a note here"
        workspace.db.session.add(ag)
        self.emitSyncCreate(ag.id, "accessGroupsList")       
        print("Handle createViewEntry request for " +  self.uri)

    # Handler for a request to update a single view entry
    def updateViewEntryHandler(self, user, workspace, key,  entry):        
        print("Handle updateViewEntryHandler request for " +  self.uri)
        ag = SpaceAccessGroup.query.filter_by(id=key).first()
        sas = SpaceAccessSpace.query.all()

        if ag is None:
            raise Exception("Update failed, group not found")
        if hasattr(entry, 'name'):
            ag.name = entry.name
        if hasattr(entry, 'note'):
            ag.note = entry.note
        if hasattr(entry, 'daily_start_time'):
            ag.daily_access_start_time = arrow.get(entry.daily_start_time, 'HH:mm')
        if hasattr(entry, 'daily_end_time'):
            ag.daily_access_end_time = arrow.get(entry.daily_end_time, 'HH:mm')
        if hasattr(entry, 'spaces'):
            ag.spaces.clear()
            for n in sas:
                if n.id in entry['spaces']:
                    ag.spaces.append(n)
        if hasattr(entry, 'days_mask'):
            ag.day_access_mask = entry.days_mask
        if hasattr(entry, 'expires_as_default'):
            ag.access_expires_as_default = entry.expires_as_default
        if hasattr(entry, 'expires_after_days'):
            ag.access_expires_default_days = entry.expires_after_days
        if hasattr(entry, 'type'):
            ag.access_type = entry.type
        if hasattr(entry, 'budget_needed'):
            ag.access_need_budget = entry.budget_needed

        self.emitSyncUpdate(key)

    # Handler for a request to update a single view entry
    def removeViewEntryHandler(self, user, workspace, key):        
        print("Handle removeViewEntryHandler request for " +  self.uri)
        ag = SpaceAccessGroup.query.filter_by(id=key).first()
        workspace.db.session.delete(ag)
        self.emitSyncRemove(key)
