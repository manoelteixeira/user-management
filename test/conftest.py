import pytest 
from os import unlink
from os import path
from app import create_app
from app import db
from app.models import User

@pytest.fixture(scope='module')
def test_user():
    new_user = User(
        username='testTuser01',
        name='First Test User',
        email='first_user@test.com',
        password='badTestPassword'
    )
    new_user.id = 1
    return new_user


@pytest.fixture(scope='module')
def test_app():
    TEST_DIR = path.abspath(path.dirname(__file__))
    test_config = path.join(TEST_DIR, 'test_app_config.cfg')
    app = create_app(test_config)
    
    if path.isfile(app.config['DATABASE_PATH']):
        unlink(app.config['DATABASE_PATH'])
    
    with app.app_context():
        try:
            db.create_all()
        except Exception as e:
            db.drop_all()
            db.create_all()
    yield app  
    unlink(app.config['DATABASE_PATH'])
    
@pytest.fixture(scope='module')
def test_db(test_app, test_user):
    new_user = User(
        username='testTuser02',
        name='Second Test User',
        email='second_user@test.com',
        password='badTestPassword2'
    )
    new_user.id = 2
    
    with test_app.app_context():
        db.session.add(test_user)
        db.session.add(new_user)
        db.session.commit()
        
        yield db 
        
@pytest.fixture(scope='module')
def test_client(test_app, test_db):
    with test_app.test_client() as test_client:
        yield test_client
        
@pytest.fixture(scope='module')
def test_logged_user(test_client, test_user):
    test_client.post('/login',
                     data=dict(username=test_user.username,
                               password='badTestPassword'),
                     follow_redirects=True)
    yield # this is where the testing happens!
    
    test_client.get('/logout',
                    follow_redirects=True)
    