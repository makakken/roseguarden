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

from datetime import datetime
from core import db, bcrypt
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method
from sqlalchemy_utils import ArrowType
import arrow
import json

from core.common.jsonDict import JsonDict
from core.users.models import User


class Message(db.Model):
    __tablename__ = 'messages'
    # nonvolatile data stored in the db
    id = db.Column(db.Integer, primary_key=True)
    recipient_email = db.Column(db.String, db.ForeignKey('users.email'))
    recipient = db.relationship("User", backref=db.backref("messages", uselist=True))
    sender_name = db.Column(db.String(120), default="")
    subject = db.Column(db.String(120), default="")
    message_html = db.Column(db.UnicodeText(), default="")
    message_send_date = db.Column(ArrowType, default=arrow.utcnow)
    message_read = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<Message from {} to {} with subject "{}" [{}] >'.format(self.sender_name, self.recipient_name,
                                                                        self.subject, message_send_date)
