import pytest

from core import create_app, db


@pytest.fixture(scope="function")
def set_up_and_tear_down_database():
    """
    This function prepares and destruct the flask application and the database
    before and after each test.
    All lines before the yield statement will be executed before the tests
    and each line after the yield statement will be called at the end of the tests
    """
    app = create_app()
    app_context = app.app_context()
    app_context.push()
    db.create_all()
    client = app.test_client()

    yield app, app_context, db, client

    db.session.remove()
    db.drop_all()
    app_context.pop()