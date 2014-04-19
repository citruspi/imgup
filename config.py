import os

class Config (object):

    SECRET_KEY = os.urandom(60).encode('hex')

    TARGET = 'uploads'
    ALLOWED = ['jpg', 'jpeg', 'gif', 'png', 'tiff']

    DIGEST = '11ae7530b0e2a72ff7e5ba6138a5a6b0e57dce2f428c5c0cbea2efad607d5a78afa4eb1c4ce52e42e393b88d7fa81e3ea818ab34d2eed2f5f0425d2dd98228ed'

class Development (Config):

    PORT = 5000
    HOST = 'localhost'

    DEBUG = True

class Production (Config):

    PORT = 8001
    HOST = 'localhost'
