import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'khj24g5kh2v5hk2vrkhqvrhkvhk2vr2hkh24vhk24sdgfgkbpih'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    # False disables signaling app every time change to database made
    SQLALCHEMY_TRACK_MODIFICATIONS = False
