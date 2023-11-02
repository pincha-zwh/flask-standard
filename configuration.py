class Config(object):
    TESTING = False
    SECRET_KEY = '192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'


class ProductionConfig(Config):
    """Production Config"""
    pass


class TestingConfig(Config):
    """Testing Config"""
    TESTING = True


class DevelopmentConfig(Config):
    """Development Config"""
    pass
