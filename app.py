from os.path import join
from os.path import abspath
from os.path import dirname

from app import create_app

if __name__ == '__main__':
    app_settings = join(abspath(dirname(__file__)), 'app_settings.cfg')
    app = create_app(app_settings)
    app.run(debug=False, host='0.0.0.0')
else:
    '''
    If app.py is runned using "flask run"
    '''
    app = create_app()