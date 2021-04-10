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


def get_accessable_spaces_for_user_string(space_access_group):
    spaces_string = ""
    for s in space_access_group.spaces:
        if spaces_string != "":
            spaces_string += ", "
        spaces_string += s.name
    if spaces_string == "":
        spaces_string = "None"
    return spaces_string


def get_user_accessable_weekdays_string(space_access_group):
    weekday_string = ""
    if space_access_group.day_access_mask & 0x01:
        if weekday_string != "":
            weekday_string += ", "
        weekday_string += "Mon."
    if space_access_group.day_access_mask & 0x02:
        if weekday_string != "":
            weekday_string += ", "
        weekday_string += "Tue."
    if space_access_group.day_access_mask & 0x04:
        if weekday_string != "":
            weekday_string += ", "
        weekday_string += "Wed."
    if space_access_group.day_access_mask & 0x08:
        if weekday_string != "":
            weekday_string += ", "
        weekday_string += "Thu."
    if space_access_group.day_access_mask & 0x10:
        if weekday_string != "":
            weekday_string += ", "
        weekday_string += "Fri."
    if space_access_group.day_access_mask & 0x20:
        if weekday_string != "":
            weekday_string += ", "
        weekday_string += "Sat."
    if space_access_group.day_access_mask & 0x40:
        if weekday_string != "":
            weekday_string += ", "
        weekday_string += "Sun."
    if weekday_string == "":
        weekday_string = "None"
    return weekday_string
