import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'khj24g5kh2v5hk2vrkhqvrhkvhk2vr2hkh24vhk24sdgfgkbpih'
