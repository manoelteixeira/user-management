'''
Test Profile Route
'''

def test_profile_change_password_no_logged_user(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/profile' page is posted (POST) with valid values for new password and no logged in user
    THEN check that the response is valid.
    """
    response = test_client.get('/profile', 
                                follow_redirects=True)
    assert response.status_code == 200
    response_data = response.data.decode()
    assert '<div class="flash">Please log in.</div>' in response_data

def test_profile_route(test_client, test_logged_user, test_user):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/profile' page is requested (GET)
    THEN check that the response is valid.
    """
    response = test_client.get('/profile', 
                                follow_redirects=True)
    assert response.status_code == 200
    response_data = response.data.decode()
    assert 'User Info' in response_data
    assert test_user.name in response_data
    assert test_user.email in response_data
    assert test_user.username in response_data
    assert str(test_user.joined_at.date()) in response_data
    assert 'Change password' in response_data
    assert 'Current password' in response_data
    assert 'Password' in response_data
    assert 'Re-enter password' in response_data
    assert 'Continue' in response_data


def test_profile_change_password_invalid_current_password(test_client, test_logged_user):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/profile' page is posted (POST) with invvalid current password
    THEN check that the response is valid.
    """
    new_password = 'NewPassword'
    response = test_client.post('/change-password',
                                data=dict(password='invalidPassword',
                                          new_password=new_password,
                                          confirm=new_password),
                                follow_redirects=True)
    assert response.status_code == 200
    response_data = response.data.decode()
    assert '<div class="flash">Password is incorrect.</div>' in response_data
    


def test_profile_change_password(test_client, test_logged_user):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/profile' page is posted (POST) with valid values for new password
    THEN check that the response is valid.
    """
    current_password = 'badTestPassword'
    new_password = 'newPassword'
    response = test_client.post('/change-password',
                                data=dict(password=current_password,
                                          new_password=new_password,
                                          confirm=new_password),
                                follow_redirects=True)
    assert response.status_code == 200
    response_data = response.data.decode()
    assert '<div class="flash">Your password has been changed.</div>' in response_data
