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

from core import db
from core.users.models import User
from core.nodes.models import Node
from sqlalchemy_utils import ArrowType
import arrow

# Define your database models here


association_table_node_spaceaccess_space = db.Table('spaceaccess_space_node_map',
    db.Column('nodes_id', db.Integer, db.ForeignKey('nodes.id')),
    db.Column('spaceaccess_space_id', db.Integer, db.ForeignKey('spaceaccess_spaces.id'))
)

class SpaceAccessSpace(db.Model):
    __tablename__ = 'spaceaccess_spaces'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), default= "")
    description = db.Column(db.String(128), default= "")
    entrance_nodes = db.relationship("Node", backref="spaceaccess_spaces", secondary=association_table_node_spaceaccess_space, lazy='subquery',)



association_table_user_accessgroup = db.Table('accessgroup_user_map',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('spaceaccess_group_id', db.Integer, db.ForeignKey('spaceaccess_groups.id'))
)

association_table_space_accessgroup = db.Table('accessgroup_space_map',
    db.Column('spaceaccess_space_id', db.Integer, db.ForeignKey('spaceaccess_spaces.id')),
    db.Column('spaceaccess_group_id', db.Integer, db.ForeignKey('spaceaccess_groups.id'))
)

# This is just a test model
class SpaceAccessGroup(db.Model):
    __tablename__ = 'spaceaccess_groups'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), default="")
    note = db.Column(db.String(120), default="")
    users = db.relationship("User", backref=db.backref("accessgroup", uselist=False), secondary=association_table_user_accessgroup, lazy='subquery',)    
    access_type = db.Column(db.String(120), default="No access")
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
    spaces = db.relationship("SpaceAccessSpace", backref=db.backref("access_group"), secondary=association_table_space_accessgroup, lazy='subquery',)    
    day_access_mask = db.Column(db.Integer, default = 0)
    daily_access_start_time = db.Column(ArrowType, default=arrow.utcnow)
    daily_access_end_time = db.Column(ArrowType, default=arrow.utcnow)

class SpaceAccessProperties(db.Model):
    __tablename__ = 'spaceaccess_properties'
    id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    access_budget = db.Column(db.Integer,default=0)
    access_need_budget = db.Column(db.Boolean, default=False)
    access_starts = db.Column(db.Boolean, default=False)
    access_expires = db.Column(db.Boolean, default=False)
    access_start_date = db.Column(ArrowType, default=arrow.utcnow)
    access_expire_date = db.Column(ArrowType, default=arrow.utcnow)
    access_last_update_date = db.Column(ArrowType, default=arrow.utcnow)
    user = db.relationship("User", backref=db.backref("access", uselist=False, 
                                cascade="save-update, merge, delete, delete-orphan"))
