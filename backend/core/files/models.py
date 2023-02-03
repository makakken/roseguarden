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
import arrow
import enum

association_table_user_filepermissiongroup = db.Table(
    "filepermissiongroup_user_map",
    db.Column("user_id", db.Integer, db.ForeignKey("users.id")),
    db.Column("filepermissiongroup_id", db.Integer, db.ForeignKey("filepermissiongroups.id")),
)


class FilePermissionGroup(db.Model):
    __tablename__ = "filepermissiongroups"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), default="")
    ldap_group = db.Column(db.String(64), default="")
    ldap = db.Column(db.Boolean, default=False)
    users = db.relationship(
        "User",
        backref="filepermission_groups",
        secondary=association_table_user_filepermissiongroup,
        lazy="subquery",
    )

    def __init__(self, name):
        self.name = name


association_table_filepermission_filepermissiongroup = db.Table(
    "filepermission_filepermissiongroup_map",
    db.Column("filepermissiongroup_id", db.Integer, db.ForeignKey("filepermissiongroups.id")),
    db.Column("filepermission_id", db.Integer, db.ForeignKey("filepermissions.id")),
)


class FilePermissionAccess(enum.IntFlag):
    NONE = 0
    READ = 1
    WRITE = 2


class FilePermission(db.Model):
    __tablename__ = "filepermissions"
    id = db.Column(db.Integer, primary_key=True)
    access = db.Column(db.Enum(FilePermissionAccess), default=FilePermissionAccess.NONE)
    groups = db.relationship(
        "FilePermissionGroup",
        backref="filepermissions",
        secondary=association_table_filepermission_filepermissiongroup,
        lazy="subquery",
    )
    ldap_group = db.Column(db.String(64), default="")
    ldap = db.Column(db.Boolean, default=False)
    name = db.Column(db.String(64), default="")
    description = db.Column(db.String(128), default="")

    def __repr__(self):
        return '<FilePermission "{}">'.format(self.name)


association_table_filepermission_filestorage = db.Table(
    "filepermission_filestorage_map",
    db.Column("filestorage_id", db.Integer, db.ForeignKey("filestorage.id")),
    db.Column("filepermission_id", db.Integer, db.ForeignKey("filepermissions.id")),
)


class FileStorageType(enum.IntFlag):
    LOCAL = 1
    NETWORK = 2
    USER = 4
    WORKSPACE = 8


class FileStorage(db.Model):
    __tablename__ = "filestorage"
    # nonvolatile data stored in the db
    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(120), default="")
    storage_type = db.Column(db.Enum(FileStorageType))
    permissions = db.relationship(
        "FilePermission",
        backref="filestorages",
        secondary=association_table_filepermission_filestorage,
        lazy="subquery",
    )

    def __repr__(self):
        return "<FileStorage {} of type:{}>".format(self.path, self.storage_type)


class GeneratedFile(db.Model):
    __tablename__ = "generatedfile"
    # nonvolatile data stored in the db
    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(120), default="")
    generated_on_date = db.Column(ArrowType, default=arrow.utcnow)
    expire_on_date = db.Column(ArrowType, default=arrow.utcnow)
    size_in_bytes = db.Column(db.Integer, default=0)
    filestorage_id = db.Column(db.Integer, db.ForeignKey("filestorage.id"))
    filestorage = db.relationship("FileStorage", backref=db.backref("generatedfiles", uselist=True))

    def __repr__(self):
        return "<GeneratedFile {} of type:{}>".format(self.path, self.generated_on_date)


class UploadedFile(db.Model):
    __tablename__ = "uploadedfile"
    # nonvolatile data stored in the db
    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(120), default="")
    generated_on_date = db.Column(ArrowType, default=arrow.utcnow)
    expire_on_date = db.Column(ArrowType, default=arrow.utcnow)
    size_in_bytes = db.Column(db.Integer, default=0)
    filestorage_id = db.Column(db.Integer, db.ForeignKey("filestorage.id"))
    filestorage = db.relationship("FileStorage", backref=db.backref("uploadedfiles", uselist=True))

    def __repr__(self):
        return "<UploadedFile {} of type:{}>".format(self.path, self.generated_on_date)
