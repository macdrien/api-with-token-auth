class Config(object):
    DEBUG = False
    TESTING = False
    JWT_SECRET_KEY='t1NP63m4wnBg6nyHYKfmc2TpCOGI4nss'
    # DATABASE_URI = 'sqlite:///:memory:'

class ProductionConfig(Config):
    pass
    # DATABASE_URI = 'mysql://user@localhost/foo'

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True