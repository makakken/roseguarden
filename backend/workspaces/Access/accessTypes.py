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

from enum import Enum


class SpaceAccessType(Enum):
    NO_ACCESS = "No access"
    UNLIMITED = "Unlimited"
    USER_BUDGET = "User Budget (days)"
    GROUP_BUDGET = "Group Budget (days)"
    AUTO_CHARGED_MONTHLY_BUDGET = "Auto-charged budget (monthly)"
    AUTO_CHARGED_WEEKLY_BUDGET = "Auto-charged budget (weekly)"


def getAccessSpacesOfNode(node):
    return []


def checkUserAccessToSpace(user, space):
    return False


def setDefaultAccessTypeUserProperties(user, access_type):
    pass
