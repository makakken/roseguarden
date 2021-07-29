import time
from core.users import userManager
from core.users.enum import UserAuthenticatorStatus
from core.workspaces import workspaceManager
from core.workspaces.workspaceHooks import WorkspaceHooks

import pytest

from core.users.models import User


@pytest.fixture(scope="function")
def high_user_count(base_setup):
    app, app_context, db, client = base_setup
    usersWorkspace = workspaceManager.getWorkspace('Users')
    for x in range(30):
        email = f'test{x}@fabba.space'
        u = User.query.filter_by(email=email).first()
        if u is None:
            u = User(email=email, password='test1234', isAdmin=False)
            u.firstname = "Test"
            u.lastname = "User"
            u.organization = "Konglomerat"
            u.account_verified = True
            u.pin = "123456"
            u.authenticator = f"0.0.0.0.{x}"
            u.authenticator_status = UserAuthenticatorStatus.VALID
            workspaceManager.triggerWorkspaceHooks(WorkspaceHooks.CREATEUSER, user=u)
            db.session.add(u)
    db.session.commit()
    all_user = User.query.all()
    print(all_user)


def test_get_user_by_authenticator_performance(high_user_count):
    before = time.time()
    # search for an nonexisitng authenticator
    userManager.getUserByAuthenticator("111.111.111.111.111", "")
    after = time.time()
    elapsed_in_seconds = after - before
    print(elapsed_in_seconds)
    # getUserByAuthenticator have to run in 3 seconds
    assert elapsed_in_seconds < 2.0
