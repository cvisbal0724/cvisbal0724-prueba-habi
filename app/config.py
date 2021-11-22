class Config:
   pass

class DevelopmentSetting(Config):
    DEBUG = True

setting = {
    'development': DevelopmentSetting,
    'default': DevelopmentSetting
}
                