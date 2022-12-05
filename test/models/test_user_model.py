'''
Test User model 
'''
from datetime import datetime

def test_new_user(test_user):
    '''
    GIVEN a new User model
    WHEN a new User is created
    THEN check the username, email, name, joined_at and password are defined correcty.
    '''
    name = 'First Test User'
    username='testTuser01'
    email='first_user@test.com'
    password='badTestPassword'
    
    assert test_user.name == name
    assert test_user.username == username
    assert test_user.email == email
    assert test_user.password != password
    assert test_user.check_password(passwd=password)
    assert test_user.joined_at <= datetime.utcnow()
    

def test_user_set_password(test_user):
    '''
    GIVEN a User model
    WHEN the method set_password is called
    THEN check if password was correctly changed
    '''
    old_password='badTestPassword'
    new_password = 'newPassword'
    
    assert test_user.password != old_password
    assert test_user.password != new_password
    assert test_user.check_password(passwd=old_password)
    assert test_user.check_password(passwd=new_password) == False
    
    test_user.set_password(passwd=new_password)
    assert test_user.password != old_password
    assert test_user.password != new_password
    assert test_user.check_password(passwd=old_password) == False
    assert test_user.check_password(passwd=new_password) 
    