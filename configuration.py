class Config(object):
    TESTING = False


class ProductionConfig(Config):
    """Production Config"""
    pass


class TestingConfig(Config):
    """Testing Config"""
    TESTING = True


class DevelopmentConfig(Config):
    """Development Config"""
    pass
