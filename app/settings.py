class Config:
   pass

class DevelopmentSetting(Config):
    DEBUG = True

setting = {
    'develop': DevelopmentSetting,
    'default': DevelopmentSetting
}
                