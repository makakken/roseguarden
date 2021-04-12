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

from datetime import datetime, time


def is_time_between(begin_time, end_time, check_time=None):
    # If check time is not given, default to current UTC time
    check_time = check_time or datetime.utcnow().time()
    return check_time >= begin_time and check_time <= end_time


def update_user_access_properties_after_user_entry(user):
    pass


def update_group_access_properties_after_user_entry(user):
    pass


def has_user_access_to_space(user, node):
    if user.spaceaccess_accessgroup is None:
        return False, "Not in an access group"
    accessgroup = user.spaceaccess_accessgroup
    if len(accessgroup.spaces) == 0:
        return False, "No spaces mapped to this node"
    for s in accessgroup.spaces:
        if s not in user.spaceaccess_accessgroup.spaces:
            return False, "User has no access to the mapped space"

    if (accessgroup.day_access_mask & (1 << datetime.today().weekday())) is 0:
        return False, "User has no access on this weekday"

    if not is_time_between(time(accessgroup.daily_access_start_time.hour, accessgroup.daily_access_start_time.minute),
                           time(accessgroup.daily_access_end_time.hour, accessgroup.daily_access_end_time.minute)):
        return False, "User has no access in this time range"

    #if datetime.now()
    # accessgroup.

    # if user.accessgroup
    return True, "Access granted"
