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

from core.nodes.nodeClass import NodeClass
from core.logs import logManager
from core.users import userManager
from core.users.enum import (
    AuthenticatorSendBy,
    AuthenticatorType,
    AuthenticatorValidityType,
)

from workspaces.Access.nodes.common.serverActionRequests import (
    UpdateUserInfoAction,
    UpdateAssignInfoAction,
    DenyAccessAction,
    GrandAccessAction,
)
from workspaces.Access.access import (
    has_user_access_to_space,
    update_user_access_properties_after_access_granted,
    is_user_budget_sufficient,
)


class DoorNoPinTerminal(NodeClass):
    class_id = "00:01:AB:EF:19:D8:00:11"
    description = "A simple door terminal without pin request"

    def defineNodeActionRequests(self):
        # general node action request
        self.defineNodeActionRequest("registerNodeStartup")
        self.defineNodeActionRequest("requestNodeUpdate")

        # node specific action request
        self.defineNodeActionRequest("requestAssignCode")
        self.defineActionProperty("requestAssignCode", "auth_key")

        self.defineNodeActionRequest("requestUserInfo")
        self.defineActionProperty("requestUserInfo", "auth_key")

        self.defineNodeActionRequest("requestUserAccess")
        self.defineActionProperty("requestUserAccess", "auth_key")
        self.defineActionProperty("requestUserAccess", "pin", optional=True)

    def handleNodeActionRequest(self, node, action, header):
        action_name = action["action"]
        public_key = ""
        if "public_key" in action:
            public_key = action["public_key"]

        if action_name == "requestNodeUpdate":
            return [{}]
        elif action_name == "requestUserInfo":
            node_action = UpdateUserInfoAction.generate(
                userManager.get_user_by_authenticator(action["auth_key"], public_key)
            )
            return [node_action]
        elif action_name == "requestUserAccess":
            user = userManager.get_user_by_authenticator(action["auth_key"], public_key)
            if user is None:
                return [DenyAccessAction.generate("Access denied", "")]

            (access, _info) = has_user_access_to_space(user, node)
            if access is False:
                return [DenyAccessAction.generate("Access denied", "")]

            if is_user_budget_sufficient(user) is False:
                return [DenyAccessAction.generate("Access denied", "Not enough budget")]

            # access gets granted
            update_user_access_properties_after_access_granted(user)
            return [GrandAccessAction.generate(user)]
        elif action_name == "requestAssignCode":
            if userManager.checkUserAuthenticatorExists(action["auth_key"], public_key) is True:
                node_action = UpdateAssignInfoAction.generate("", False)
            else:
                code = userManager.createUserAuthenticatorRequest(
                    action["auth_key"],
                    public_key,
                    AuthenticatorType.USER,
                    AuthenticatorValidityType.ONCE,
                    AuthenticatorSendBy.NODE,
                    self.identity["nodename"],
                )
                node_action = UpdateAssignInfoAction.generate(code, True)
            return [node_action]
        else:
            return [{}]
