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

from core import db
from sqlalchemy_utils import ArrowType
from workspaces.Access.types import SpaceAccessType
import arrow


# Define your database models here
class SpaceNodeMap(db.Model):
    __tablename__ = 'spaceaccess_space_node_map'
    id = db.Column(db.Integer, primary_key=True)
    node_id = db.Column(db.Integer(), db.ForeignKey('nodes.id'))
    space_id = db.Column(db.Integer(), db.ForeignKey('spaceaccess_spaces.id'))


class AccessgroupSpaceMap(db.Model):
    __tablename__ = 'spaceaccess_accessgroup_space_map'
    id = db.Column(db.Integer, primary_key=True)
    space_id = db.Column(db.Integer(), db.ForeignKey('spaceaccess_spaces.id'))
    group_id = db.Column(db.Integer(), db.ForeignKey('spaceaccess_groups.id'))


class AccessgroupUserMap(db.Model):
    __tablename__ = 'spaceaccess_accessgroup_user_map'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))
    group_id = db.Column(db.Integer(), db.ForeignKey('spaceaccess_groups.id'))


class SpaceAccessSpace(db.Model):
    __tablename__ = 'spaceaccess_spaces'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), default="")
    description = db.Column(db.String(128), default="")
    entrance_nodes = db.relationship(
        "Node",
        backref=db.backref("spaceaccess_spaces", lazy=True),
        secondary=SpaceNodeMap.__tablename__,
        lazy='subquery',
    )


class SpaceAccessGroup(db.Model):
    __tablename__ = 'spaceaccess_groups'
    id = db.Column(db.Integer, primary_key=True)
    users = db.relationship(
        "User",
        backref=db.backref("spaceaccess_accessgroup", uselist=False, lazy=True),
        secondary=AccessgroupUserMap.__tablename__,
        lazy='subquery',
    )
    spaces = db.relationship(
        "SpaceAccessSpace",
        backref=db.backref("spaceaccess_accessgroup", lazy=True),
        secondary=AccessgroupSpaceMap.__tablename__,
        lazy='subquery',
    )
    name = db.Column(db.String(120), default="")
    note = db.Column(db.String(120), default="")
    access_type = db.Column(db.Enum(SpaceAccessType), default=SpaceAccessType.NO_ACCESS)
    access_need_budget = db.Column(db.Boolean, default=False)
    access_autocharged = db.Column(db.Boolean, default=False)
    access_autocharge_budget_amount = db.Column(db.Boolean, default=False)
    access_autocharge_budget_period = db.Column(db.String(120), default="monthly")
    access_autocharge_budget_period_count = db.Column(db.Integer, default=1)
    access_autocharge_budget_cut = db.Column(db.Boolean, default=True)
    access_autocharge_budget_max = db.Column(db.Integer, default=0)
    access_expires_as_default = db.Column(db.Boolean, default=False)
    access_expires_default_days = db.Column(db.Integer, default=365)
    group_budget = db.Column(db.Integer, default=0)
    day_access_mask = db.Column(db.Integer, default=0)
    daily_access_start_time = db.Column(ArrowType, default=arrow.utcnow)
    daily_access_end_time = db.Column(ArrowType, default=arrow.utcnow)


class SpaceAccessProperties(db.Model):
    __tablename__ = 'spaceaccess_properties'
    id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    access_budget = db.Column(db.Integer, default=0)
    access_need_budget = db.Column(db.Boolean, default=False)
    access_starts = db.Column(db.Boolean, default=False)
    access_expires = db.Column(db.Boolean, default=False)
    access_start_date = db.Column(ArrowType, default=arrow.utcnow)
    access_expire_date = db.Column(ArrowType, default=arrow.utcnow)
    access_last_update_date = db.Column(ArrowType, default=arrow.utcnow)
    user = db.relationship("User",
                           backref=db.backref("access",
                                              uselist=False,
                                              cascade="save-update, merge, delete, delete-orphan"))
