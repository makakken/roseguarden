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

from core.workspaces.page import Page

""" The user account page
"""


class Account(Page):
    title = "Account"  # Shown label of the page in the menu
    group = "User"  # groupname multiple pages
    icon = "face"  # icon (in typeset of material design icons)
    route = "/user/account"  # routing
    builder = "frontend"  # page get build by the client (frontend)
    rank = 10.1  # ranks (double) the page higher values are at the top of the menu
    # groups will be ranked by the sum of the rank-values of their entries
    requireLogin = True  # login is required to view the page
    requirePermission = None  # No permission is rewuired to view the page, the value have to be defined
    # can be None, Permission or a list of Permissions
    requireAdmin = False  # login dont need admin privileges
