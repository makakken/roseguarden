"""
The roseguarden project

Copyright (C) 2018-2021  Marcus Drobisch,

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


def hasUserAccessToSpace(user, node):
    if user.accessgroup is None:
        return False, "Not in an access group"
    if len(node.spaceaccess_spaces) == 0:
        return False, "No spaces mapped to this node"
    for s in node.spaceaccess_spaces:
        if s not in user.accessgroup.spaces:
            return False, "User has no access to the mapped space"

    # if user.accessgroup
    return True, "Access granted"
