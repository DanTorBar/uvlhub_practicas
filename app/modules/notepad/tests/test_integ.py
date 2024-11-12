import pytest
from app import db
from app.modules.conftest import login, logout
from app.modules.auth.models import User
from app.modules.profile.models import UserProfile
from app.modules.notepad.models import Notepad


@pytest.fixture(scope='module')
def test_client(test_client):
    """
    Extends the test_client fixture to add additional specific data for module testing.
    for module testing (por example, new users)
    """
    with test_client.application.app_context():
        user_test = User(email='user@example.com', password='test1234')
        db.session.add(user_test)
        db.session.commit()

        profile = UserProfile(user_id=user_test.id, name="Name", surname="Surname")
        db.session.add(profile)
        db.session.commit()
        

    yield test_client


def test_list_empty_notepad_get(test_client):
    """
    Tests access to the empty notepad list via GET request.
    """
    login_response = login(test_client, "user@example.com", "test1234")
    assert login_response.status_code == 200, "Login was unsuccessful."

    response = test_client.get("/notepad")
    assert response.status_code == 200, "The notepad page could not be accessed."
    assert b"You have no notepads." in response.data, "The expected content is not present on the page"

    logout(test_client)
    
'''
CREATE
'''
def test_list_not_empty_notepad_get(test_client):
    """
    Tests access to the empty notepad list via GET request.
    """
    login_response = login(test_client, "user@example.com", "test1234")
    assert login_response.status_code == 200, "Login was unsuccessful."

    
    response = test_client.post(
        "/notepad/create", data=dict(title="Prueba", body="pruebita probada"), follow_redirects=True
    )
    
    
    assert b"Prueba" in response.data, "The expected content is not present on the page"

    logout(test_client)        

'''
READ BY ID
'''
def test_show_notepad(test_client):

    user_test = User(email='user2@example.com', password='test1234')
    db.session.add(user_test)
    db.session.commit()
    
    login_response = login(test_client, "user2@example.com", "test1234")
    assert login_response.status_code == 200, "Login was unsuccessful."

    notepad = Notepad(title="Notepad detallado", body=f"este es notepad con muchos detalles entre ellos indica que la palabara secreta es {"lolinto"}", user_id=user_test.id)
    db.session.add(notepad)
    db.session.commit()

    response = test_client.get(f"/notepad/{notepad.id}")

    assert b"lolinto" in response.data, "The expected content is not present on the page"

    logout(test_client)    
    

'''
EDIT
'''
def test_update_notepad(test_client):

    user_test = User(email='user3@example.com', password='test1234')
    db.session.add(user_test)
    db.session.commit()
    
    login_response = login(test_client, "user3@example.com", "test1234")
    assert login_response.status_code == 200, "Login was unsuccessful."

    notepad = Notepad(title="Prueba", body="este es notepad creado", user_id=user_test.id)
    db.session.add(notepad)
    db.session.commit()

    response1 = test_client.get("/notepad")

    assert b"Prueba" in response1.data, "The expected content is not present on the page"


    response2 = test_client.post(
        f"/notepad/edit/{notepad.id}", data=dict(title="Notepad-editado", body="lerele lerele lerele"), follow_redirects=True
    )

    
    assert b"Notepad-editado" in response2.data, "The expected content is not present on the page"

    logout(test_client)    
    
'''
DELETE
'''
def test_delete_notepad(test_client):

    user_test = User(email='user4@example.com', password='test1234')
    db.session.add(user_test)
    db.session.commit()
    
    login_response = login(test_client, "user4@example.com", "test1234")
    assert login_response.status_code == 200, "Login was unsuccessful."

    notepad = Notepad(title="Notepad", body="este es un notepad creado", user_id=user_test.id)
    db.session.add(notepad)
    db.session.commit()

        
    response = test_client.post(f"/notepad/delete/{notepad.id}", follow_redirects=True)    
    
    assert b"You have no notepads." in response.data, "The expected content is not present on the page"

    logout(test_client)